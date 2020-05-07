from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic, View
from django.contrib.auth import login, authenticate
from apps.publications.models import StoryPublication, StoryChapter
from apps.users.models import CustomUser, UserProfile
from apps.users.forms import CustomUserCreationForm, MailCheck, UsernameCheck, CreateUserProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.forms import AuthenticationForm
from social_django.utils import psa, load_strategy
from django.db import transaction, IntegrityError
from social_django.models import UserSocialAuth
from django.conf import settings
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from .token import account_activation_token
from django.core.mail import EmailMessage




#retorna el perfil del usuario
class ListUserPerfil(LoginRequiredMixin, generic.DetailView):
    model = CustomUser
    template_name = 'users/user_profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_object(self):
        return get_object_or_404(CustomUser, username=self.kwargs.get('username'), is_active=True)

    def get_context_data(self, **kwargs):
        context = super(ListUserPerfil, self).get_context_data(**kwargs)
        from_user = self.request.user
        to_user = self.get_object()
        is_following = from_user.profile.get().from2To.filter(to_user = to_user.profile.get()).exists()
        context.update({'is_following': is_following})
        context.update({'customuser': to_user})
        publications = StoryPublication.objects.filter(own_user = to_user.profile.get(), active=True).order_by('date_time__month', '-date_time__day')
        context.update({'storypublication_list': publications})
        chaps = StoryChapter.objects.filter(own_user = to_user.profile.get(), active=True).order_by('date_time__month', '-date_time__day')
        context.update({'storychapter_list': chaps})
        return context

#para listar los followers
class ListUserFollowers(LoginRequiredMixin, generic.DetailView):
    template_name = 'users/followers.html'
    model = CustomUser
    slug_field = 'username'
    slug_url_kwarg = 'username' 

    def get_context_data(self, **kwargs):
        context = super(ListUserFollowers, self).get_context_data(**kwargs)
        followers = self.object.profile.get().to2From.all()
        context.update({'followers': followers})
        return context


#para listar los followings
class ListUserFollowing(LoginRequiredMixin, generic.DetailView):
    template_name = 'users/following.html'
    model = CustomUser
    slug_field = 'username'
    slug_url_kwarg = 'username' 

    def get_context_data(self, **kwargs):
        context = super(ListUserFollowing, self).get_context_data(**kwargs)
        following = self.object.profile.get().from2To.all()
        context.update({'following': following})
        return context


#para listar las subscripciones a stories de un usuario
class ListStoriesSubscription(LoginRequiredMixin, generic.ListView):
    template_name = 'publications/story/story_subscription.html'
    models = StoryPublication
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(CustomUser, username=self.kwargs["username"])
        qs = user.profile.get().pub_subscription.filter(active=True)
        return qs

    def get_context_data(self, **kwargs):
        context = super(ListStoriesSubscription, self).get_context_data(**kwargs)
        context.update({'customuser': {'username':self.kwargs["username"]}})
        return context

#agregar seguidor a user.
class FollowUser(LoginRequiredMixin, generic.DetailView):
    model = CustomUser
    slug_field = 'username'
    slug_url_kwarg = 'username' 

    def get(self, request, username):
        self.request.user.profile.get().user_subscription.add(self.get_object().profile.get());
        return redirect(reverse_lazy('user:user_profile', kwargs={'username': username}))

#unfollow user
class UnfollowUser(LoginRequiredMixin, generic.DetailView):
    model = CustomUser
    slug_field = 'username'
    slug_url_kwarg = 'username' 

    def get(self, request, username):
        self.request.user.profile.get().user_subscription.remove(self.get_object().profile.get());
        return redirect(reverse_lazy('user:user_profile', kwargs={'username': username}))

#para dar de alta un usuario
class SignUpView(generic.CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        #form2 = AuthenticationForm()
        #context.update({'loginform': form2})
        return context


    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        '''username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)'''
        return redirect(reverse_lazy('fill_profile', kwargs = {'uidb64': urlsafe_base64_encode(force_bytes(user.pk))}))

class FillProfile(generic.CreateView):
    model = UserProfile
    form_class = CreateUserProfile
    template_name = 'registration/fill_user_profile.html'

    def form_valid(self, form, **kwargs):
        id = force_text(urlsafe_base64_decode(self.kwargs.get('uidb64')))
        user = CustomUser.objects.get(id = id)
        if (user and not user.profile.exists()): #exists por las dudas que inyecten en la url un uidb64 de un usuario ya creado.
            profile = form.save(commit=False)
            profile.user = user;
            profile.save()
            send_mail_confirm(self.request, user)
            return redirect(reverse_lazy('hall_s', kwargs={'success': True}))
        else:
            return redirect('/')

class ActivateAccount(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token) and not user.is_active:
            user.is_active = True
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect(reverse_lazy('hall_a', kwargs={'activated': True}))
        else:
            return redirect(reverse_lazy('hall_a', kwargs={'activated': False}))

def send_mail_confirm(request, user):
    current_site = get_current_site(request)
    mail_subject = 'Registro de usuario.'
    message = render_to_string('registration/activate_account.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    to_email = user.email
    email = EmailMessage(
                mail_subject, message, to=[to_email]
    )
    email.content_subtype = "html"
    email.send()


#Eliminar usuario. No se eliminan, se ponen inactivos
class DeleteUser(LoginRequiredMixin, generic.DeleteView):
    def get(self, request, username, id):
        user = CustomUser.objects.get(id=request.user.id)
        userDel = CustomUser.objects.get(id=id)
        if (userDel == user):
            user.is_active=False
            user.save(update_fields=['is_active'])

        return redirect(request.GET.get('logout')) #revisar ese get(logout)

#buscar un usuario
class SearchUser(LoginRequiredMixin, generic.DetailView):
    def get(self, *args, **kwargs):
        if (self.request.is_ajax()):
            users = CustomUser.objects.filter(username__icontains=self.kwargs.get('suser'), is_active=True)[:5]
            us = []
            res_users = dict()
            for x in users:
                user = {}
                user.update({'username': x.username})
                user.update({'url': reverse('user:user_profile', kwargs={'username': x.username})})
                us.append(user)
            res_users.update({'users_found': us})
            return JsonResponse(res_users)

'''renderiza el template para pedir el email, en caso de qeu destilde la casilla cuando inicie sesion con fb, o si el mail es duplicado.'''
class mail_check(generic.edit.FormView):
    form_class = MailCheck
    template_name = 'registration/force_get_email.html'
    success_url = reverse_lazy('social:complete', kwargs={"backend":"facebook"})

    def get_context_data(self, **kwargs):
        context = super(mail_check, self).get_context_data(**kwargs)
        strategy = load_strategy()
        partial_token = self.request.GET.get('partial_token')
        partial = strategy.partial_load(partial_token)
        context.update({
            'partial_backend_name': partial.backend,
            'partial_token': partial_token
        })
        return context

    #si el form es valido, se guardar email en una variable de sesion para que el partial pipeline la obtenga.
    def form_valid(self, form):
        self.request.session['email'] = form.cleaned_data['email']
        return super().form_valid(form)

'''renderiza el template para pedir un nuevo username, en caso que sea duplicado.'''
class username_check(generic.edit.FormView):
    form_class = UsernameCheck
    template_name = 'registration/new_username.html'
    success_url = reverse_lazy('social:complete', kwargs={"backend":"facebook"})

    def get_context_data(self, **kwargs):
        context = super(username_check, self).get_context_data(**kwargs)
        strategy = load_strategy()
        partial_token = self.request.GET.get('partial_token')
        partial = strategy.partial_load(partial_token)
        context.update({
            'partial_backend_name': partial.backend,
            'partial_token': partial_token
        })
        return context

    #si el form es valido, se guarda el username en una variable de sesion para que el partial pipeline la obtenga.
    def form_valid(self, form):
        self.request.session['username'] = form.cleaned_data['username']
        return super().form_valid(form)

'''renderiza el template para pedir un nuevo username, en caso que sea duplicado.'''
class LoginView(generic.edit.FormView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context.update({'success': self.kwargs.get('success',None)})
        context.update({'activated': self.kwargs.get('activated',None)})
        return context


