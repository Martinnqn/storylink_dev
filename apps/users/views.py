from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic, View
from django.contrib.auth import login, authenticate
from apps.publications.models import StoryPublication, StoryChapter
from apps.users.models import CustomUser, UserProfile
from apps.users.forms import CustomUserCreationForm, MailCheck, UsernameCheck, CreateUserProfile, AuthenticationFormWithInactiveUsersOkay
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

#para dar de alta un usuario. Cuando crea el usuario le envia un mail para verificar la cuenta.
class SignUpView(generic.CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        context.update({'formSignUp': self.get_form()})
        context.update({'formLogin': AuthenticationFormWithInactiveUsersOkay})
        return context

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        send_mail_confirm(self.request, user)
        return redirect(reverse_lazy('hall_s', kwargs = {'success': True}))

'''
CustomloginView permite iniciar sesion solo si un usuario tiene el email verificado y ademas tiene el UserProfile creado
(no checkea is_active en CustomUser).
Si el email no esta verificado el formulario lanza is_invalid. Si el mail esta verificado y el usuario aun no tiene creado
su UserProfile, entonces se lo redirige a FillProfile para que pueda crear su profile.
Si el usuario tiene el mail verificado, y se inicia sesion, se verifica si su estado era activo o inactivo,
para actualizarlo.'''
class CustomLoginView(generic.edit.FormView):
    form_class = AuthenticationFormWithInactiveUsersOkay
    template_name = 'registration/login.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(CustomLoginView, self).get_context_data(**kwargs)
        context.update({'success': self.kwargs.get('success', None)})
        context.update({'formSignUp': CustomUserCreationForm})
        context.update({'formLogin': self.get_form()})
        return context

    def form_valid(self, form):
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            if(user.profile.exists()):
                if (user.is_active):
                    login(self.request, user)
                    return redirect('/')
                else:
                    #este caso es por si un usuario habia desactivado su cuenta a proposito, y luego volvio a iniciar sesion.
                    user.is_active = True
                    user.save()
                    login(self.request, user)
                    return redirect('/', kwargs = {'is_reactive': True}) #WARNINGGGGG hacer esta url
            else:
                #se redirige para que complete su perfil.
                return redirect(reverse_lazy('fill_profile', kwargs = {'uidb64': urlsafe_base64_encode(force_bytes(user.pk))}))
        else:
            return redirect('/') #no se por que llegaria a este else. (El form lanza error si el usuario no existe, o si el usuario no verifico su mail)

    def form_invalid(self, form):
        return super().form_invalid(form)

'''Permite cargar los datos de un perfil si su email ya fue verificado. Luego de cargar los datos inicia sesion.
Si el perfil ya existia entonces omite la consulta. Si se intenta acceder a la url sin estar el mail verificado 
redirige al /. Resulta un poco inseguro permitir que un usuario se loguee, ya que no se esta pidiendo la password,
y no se esta accediendo desde una url con token de seguridad. Pero las probabilidades de que alguien intersecte 
el uid de un usuario nuevo que acaba de verificar el mail son muy pequenias.
'''
class FillProfile(generic.CreateView):
    model = UserProfile
    form_class = CreateUserProfile
    template_name = 'registration/fill_user_profile.html'

    def get_context_data(self, **kwargs):
        context = super(FillProfile, self).get_context_data(**kwargs)
        context.update({'email_verified': self.kwargs.get('email_verified', None)})
        return context

    def form_valid(self, form, **kwargs):
        id = force_text(urlsafe_base64_decode(self.kwargs.get('uidb64')))
        user = get_object_or_404(CustomUser, id = id, email_verified=True)
        if (user and not user.profile.exists()): #exists por las dudas que inyecten en la url un uidb64 de un usuario ya creado.
            try:
                with transaction.atomic():
                    profile = form.save(commit=False)
                    profile.user = user
                    user.is_active = True
                    user.save()
                    profile.save()
            except IntegrityError as e:
                print("Errorrrrr "+e.message)
            login(self.request, user, backend='django.contrib.auth.backends.AllowAllUsersModelBackend')
            return redirect(reverse_lazy('hall_a', kwargs={'activated': True}))
        else:
            return redirect('/')

    def get(self, *args, **kwargs):
        id = force_text(urlsafe_base64_decode(self.kwargs.get('uidb64')))
        existUser = CustomUser.objects.filter(id = id, email_verified=True).exists()
        if (existUser):
            return super().get(*args, **kwargs)
        else:
            return redirect('/')
        
#verificar si es necesario calcular el uid de nuevo para el fillprofile. Creo es siempre el mismo.
class VerifiedMail(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token) and not user.is_active:
            user.email_verified = True
            user.save()
            return redirect(reverse_lazy('fill_profile', kwargs = {'uidb64': urlsafe_base64_encode(force_bytes(user.pk)), 'email_verified': True}))
        else:
            return redirect(reverse_lazy('hall_a', kwargs={'email_verified': False}))

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


class EditUserProfile(LoginRequiredMixin, generic.edit.UpdateView):
    model = UserProfile
    form_class = EditUserProfile
    template_name = 'users/edit_profile.html'

    def get_success_url(self):
        return reverse_lazy('user:user_profile', kwargs={'username': self.request.user.username})

    def get_object(self, queryset=None):
        return self.request.user.profile.get()

    def get_context_data(self, **kwargs):
        context = super(EditUserProfile, self).get_context_data(**kwargs)
        context.update({'customuser': {'username': self.request.user.username}})
        return context

class EditUserAccount(LoginRequiredMixin, generic.edit.UpdateView):
    model = CustomUser
    form_class = EditAccount
    template_name = 'users/edit_user_account.html'

    def get_success_url(self):
        return reverse_lazy('user:user_profile', kwargs={'username': self.request.user.username})

    def get_object(self, queryset=None):
        return get_object_or_404(CustomUser, id = self.request.user.id);

    def get_context_data(self, **kwargs):
        context = super(EditUserAccount, self).get_context_data(**kwargs)
        context.update({'customuser': {'username': self.request.user.username}})
        print("get context data retornaaa")
        print(self.request.user.username)
        return context