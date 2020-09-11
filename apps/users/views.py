from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic, View
from django.contrib.auth import login, authenticate
from apps.publications.models import StoryPublication, StoryChapter
from apps.users.models import CustomUser, UserProfile
from apps.users.forms import (
    CustomUserCreationForm,
    MailCheck,
    UsernameCheck,
    CreateUserProfile,
    AuthenticationFormWithInactiveUsersOkay,
)
from apps.users.forms import EditUserProfile, EditAccount
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from social_django.utils import load_strategy
from django.db import transaction, IntegrityError
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from .token import account_activation_token
from django.core.mail import EmailMessage


class ReactV(generic.TemplateView):
    template_name = "test.html"


class ListUserPerfil(LoginRequiredMixin, generic.DetailView):
    """Return UserProfile visited. (username of the visited profile is obtained
    from the url parameter)"""

    model = CustomUser
    template_name = "users/user_profile.html"
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_object(self):
        return get_object_or_404(CustomUser, username=self.kwargs.get("username"), is_active=True)

    def get_context_data(self, **kwargs):
        context = super(ListUserPerfil, self).get_context_data(**kwargs)
        from_user = self.request.user
        to_user = self.get_object()
        is_following = (
            from_user.profile.get().from2To.filter(to_user=to_user.profile.get()).exists()
        )
        context.update({"is_following": is_following})
        context.update({"customuser": to_user})
        publications = StoryPublication.objects.get_stories_by_user(to_user, from_user).order_by(
            "date_time__month", "-date_time__day"
        )
        context.update({"storypublication_list": publications})
        chaps = StoryChapter.objects.get_chapters_by_user(to_user, from_user).order_by(
            "date_time__month", "-date_time__day"
        )
        context.update({"storychapter_list": chaps})
        return context


class ListUserFollowers(LoginRequiredMixin, generic.DetailView):
    """List followers from username url kwarg"""

    template_name = "users/followers.html"
    model = CustomUser
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        context = super(ListUserFollowers, self).get_context_data(**kwargs)
        followers = self.object.profile.get().to2From.all()
        context.update({"followers": followers})
        return context


class ListUserFollowing(LoginRequiredMixin, generic.DetailView):
    """List followings from username url kwarg"""

    template_name = "users/following.html"
    model = CustomUser
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        context = super(ListUserFollowing, self).get_context_data(**kwargs)
        following = self.object.profile.get().from2To.all()
        context.update({"following": following})
        return context


class ListStoriesSubscription(LoginRequiredMixin, generic.ListView):
    """List the user stories subscriptions"""

    template_name = "publications/story/story_subscription.html"
    models = StoryPublication
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(CustomUser, username=self.kwargs["username"])
        qs = user.profile.get().pub_subscription.filter(active=True)
        return qs


class FollowUser(LoginRequiredMixin, generic.DetailView):
    """Add follower to user."""

    model = CustomUser
    slug_field = "username"
    slug_url_kwarg = "username"

    def get(self, request, username):
        self.request.user.profile.get().user_subscription.add(self.get_object().profile.get())
        return redirect(reverse_lazy("user:user_profile", kwargs={"username": username}))


class UnfollowUser(LoginRequiredMixin, generic.DetailView):
    """unfollow user"""

    model = CustomUser
    slug_field = "username"
    slug_url_kwarg = "username"

    def get(self, request, username):
        self.request.user.profile.get().user_subscription.remove(self.get_object().profile.get())
        return redirect(reverse_lazy("user:user_profile", kwargs={"username": username}))


class SignUpView(generic.CreateView):
    """User SignUp. After create user, sends a email for verify user and email."""

    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "registration/login.html"

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        context.update({"formSignUp": self.get_form()})
        context.update({"formLogin": AuthenticationFormWithInactiveUsersOkay})
        return context

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        send_mail_confirm(self.request, user)
        return redirect(reverse_lazy("hall_s", kwargs={"success": True}))


class CustomLoginView(generic.edit.FormView):
    """
    CustomloginView allow login only if the user has the verified email and has
    created UserProfile (this custom login does not checks is_active in
    CustomUser, like default login).
    If the email is not verified, the form returns ValidationError with
    code=email_not_verified.
    If email is verified and the user has not yet created their UserProfile,
    it redirects you to FillProfile View so they can create their profile.
    If the user has email verified and do log in, verifies if their status was
    active or inactive, for update it."""

    form_class = AuthenticationFormWithInactiveUsersOkay
    template_name = "registration/login.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super(CustomLoginView, self).get_context_data(**kwargs)
        context.update({"success": self.kwargs.get("success", None)})
        context.update({"formSignUp": CustomUserCreationForm})
        context.update({"formLogin": self.get_form()})
        return context

    def form_valid(self, form):
        username = self.request.POST["username"]
        password = self.request.POST["password"]
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            if user.profile.exists():
                if user.is_active:
                    login(self.request, user)
                    return redirect("/")
                else:
                    # este caso es por si un usuario desactivo su cuenta
                    # a proposito, y luego volvio a iniciar sesion.
                    user.is_active = True
                    user.save()
                    login(self.request, user)
                    # WARNINGGGGG hacer esta url
                    return redirect("/", kwargs={"is_reactive": True})
            else:
                # se redirige para que complete su perfil.
                return redirect(
                    reverse_lazy(
                        "fill_profile",
                        kwargs={"uidb64": urlsafe_base64_encode(force_bytes(user.pk))},
                    )
                )
        else:
            # no se por que llegaria a este else. (El form lanza error si el
            # usuario no existe, o si el usuario no verifico su mail)
            return redirect("/")

    def form_invalid(self, form):
        return super().form_invalid(form)


class FillProfile(generic.CreateView):
    """Allow load the profile data, if you email has already been verified verified.

    After loading the data, log in.
    If the profile already exists, then skip the query.
    If you try to access the url without the email being verified, it redirects
    you to /.
    This url should have a token of security, because doesn't require password
    to reach this View. (A hacker can try fillprofile/<uidb64>/ until discover a
    valid URL).
    """

    model = UserProfile
    form_class = CreateUserProfile
    template_name = "registration/fill_user_profile.html"

    def get_context_data(self, **kwargs):
        context = super(FillProfile, self).get_context_data(**kwargs)
        context.update({"email_verified": self.kwargs.get("email_verified", None)})
        return context

    def form_valid(self, form, **kwargs):
        id = force_text(urlsafe_base64_decode(self.kwargs.get("uidb64")))
        user = get_object_or_404(CustomUser, id=id, email_verified=True)
        # exists por las dudas que inyecten en la url un uidb64 de un usuario ya creado.
        if user and not user.profile.exists():
            try:
                with transaction.atomic():
                    profile = form.save(commit=False)
                    profile.user = user
                    user.is_active = True
                    user.save()
                    profile.save()
            except IntegrityError as e:
                print("Errorrrrr " + e.message)
            login(
                self.request, user, backend="django.contrib.auth.backends.AllowAllUsersModelBackend"
            )
            return redirect(reverse_lazy("hall_a", kwargs={"activated": True}))
        else:
            return redirect("/")

    def get(self, *args, **kwargs):
        id = force_text(urlsafe_base64_decode(self.kwargs.get("uidb64")))
        existUser = CustomUser.objects.filter(id=id, email_verified=True).exists()
        if existUser:
            return super().get(*args, **kwargs)
        else:
            return redirect("/")


class VerifyMail(View):
    """Verify the email associated to a user"""

    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None
        if (
            user is not None
            and account_activation_token.check_token(user, token)
            and not user.is_active
        ):
            user.email_verified = True
            user.save()
            return redirect(
                reverse_lazy(
                    "fill_profile",
                    kwargs={
                        "uidb64": urlsafe_base64_encode(force_bytes(user.pk)),
                        "email_verified": True,
                    },
                )
            )
        else:
            return redirect(reverse_lazy("hall_a", kwargs={"email_verified": False}))


def send_mail_confirm(request, user):
    current_site = get_current_site(request)
    mail_subject = "Registro de usuario."
    message = render_to_string(
        "registration/activate_account.html",
        {
            "user": user,
            "domain": current_site.domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": account_activation_token.make_token(user),
        },
    )
    to_email = user.email
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.content_subtype = "html"
    email.send()


class DeleteUser(LoginRequiredMixin, generic.DeleteView):
    """Soft delete user. They are not deleted, they just become inactive"""

    def get(self, request, username, id):
        user = CustomUser.objects.get(id=request.user.id)
        userDel = CustomUser.objects.get(id=id)
        if userDel == user:
            user.is_active = False
            user.save(update_fields=["is_active"])

        return redirect(request.GET.get("logout"))  # revisar ese get(logout)


class SearchUser(LoginRequiredMixin, generic.DetailView):
    def get(self, *args, **kwargs):
        if self.request.is_ajax():
            users = CustomUser.objects.filter(
                username__icontains=self.kwargs.get("suser"), is_active=True
            )[:5]
            us = []
            res_users = dict()
            for x in users:
                user = {}
                user.update({"username": x.username})
                user.update({"url": reverse("user:user_profile", kwargs={"username": x.username})})
                us.append(user)
            res_users.update({"users_found": us})
            return JsonResponse(res_users)


class mail_check(generic.edit.FormView):
    """Requests the email, in case it is not sent by the provider, or if the
    email is duplicated."""

    form_class = MailCheck
    template_name = "registration/force_get_email.html"
    success_url = reverse_lazy("social:complete", kwargs={"backend": "facebook"})

    def get_context_data(self, **kwargs):
        context = super(mail_check, self).get_context_data(**kwargs)
        strategy = load_strategy()
        partial_token = self.request.GET.get("partial_token")
        partial = strategy.partial_load(partial_token)
        context.update({"partial_backend_name": partial.backend, "partial_token": partial_token})
        return context

    # si el form es valido, se guardar email en una variable de sesion para que el partial pipeline la obtenga.
    def form_valid(self, form):
        self.request.session["email"] = form.cleaned_data["email"]
        return super().form_valid(form)


class username_check(generic.edit.FormView):
    """Request for a new username, in case it is already in use."""

    form_class = UsernameCheck
    template_name = "registration/new_username.html"
    success_url = reverse_lazy("social:complete", kwargs={"backend": "facebook"})

    def get_context_data(self, **kwargs):
        context = super(username_check, self).get_context_data(**kwargs)
        strategy = load_strategy()
        partial_token = self.request.GET.get("partial_token")
        partial = strategy.partial_load(partial_token)
        context.update({"partial_backend_name": partial.backend, "partial_token": partial_token})
        return context

    # si el form es valido, se guarda el username en una variable de sesion para que el partial pipeline la obtenga.
    def form_valid(self, form):
        self.request.session["username"] = form.cleaned_data["username"]
        return super().form_valid(form)


class EditUserProfile(LoginRequiredMixin, generic.edit.UpdateView):
    model = UserProfile
    form_class = EditUserProfile
    template_name = "users/edit_profile.html"

    def get_success_url(self):
        return reverse_lazy("user:user_profile", kwargs={"username": self.request.user.username})

    def get_object(self, queryset=None):
        return self.request.user.profile.get()

    def get_context_data(self, **kwargs):
        context = super(EditUserProfile, self).get_context_data(**kwargs)
        context.update({"customuser": {"username": self.request.user.username}})
        return context


class EditUserAccount(LoginRequiredMixin, generic.edit.UpdateView):
    model = CustomUser
    form_class = EditAccount
    template_name = "users/edit_user_account.html"

    def get_success_url(self):
        self.request.user.refresh_from_db()
        return reverse_lazy("user:user_profile", kwargs={"username": self.request.user.username})

    def get_object(self, queryset=None):
        return get_object_or_404(CustomUser, id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super(EditUserAccount, self).get_context_data(**kwargs)
        context.update({"customuser": {"username": self.request.user.username}})
        return context
