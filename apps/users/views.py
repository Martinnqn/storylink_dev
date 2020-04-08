from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic, View
from django.contrib.auth import login, authenticate
from apps.publications.models import StoryPublication, StoryChapter
from apps.users.models import CustomUser
from apps.users.forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.forms import AuthenticationForm


    
#Obtiene todos los datos necesarios para que el menu del perfil de un usuario funcione. 
'''Todas las clases que utilicen un template que muestre el menu del usuario deben heredar de esta clase. 
(Cualquier template que herede de users/profile_base.html)'''
class ListUserDataMenuPerfil(LoginRequiredMixin, generic.DetailView):
    model = CustomUser
    template_name = 'users/user_profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username' 

    def get_context_data(self, **kwargs):
        context = super(ListUserDataMenuPerfil, self).get_context_data(**kwargs)
        from_user = self.request.user
        to_user = get_object_or_404(CustomUser, username=self.kwargs.get('username'))
        is_following = from_user.from2To.filter(to_user = to_user).exists()
        context.update({'is_following': is_following})
        context.update({'customuser': to_user})
        publications = StoryPublication.objects.filter(own_user = to_user, active=True)
        context.update({'list_pub': publications})
        chaps = StoryChapter.objects.filter(own_user = to_user, active=True)
        context.update({'chapters': chaps})
        return context

#para listar los followers
class ListUserFollowers(LoginRequiredMixin, generic.DetailView):
    template_name = 'users/followers.html'
    model = CustomUser
    slug_field = 'username'
    slug_url_kwarg = 'username' 

    def get_context_data(self, **kwargs):
        context = super(ListUserFollowers, self).get_context_data(**kwargs)
        followers = self.object.to2From.all()
        context.update({'followers': followers})
        print(context)
        return context


#para listar los followings
class ListUserFollowing(LoginRequiredMixin, generic.DetailView):
    template_name = 'users/following.html'
    model = CustomUser
    slug_field = 'username'
    slug_url_kwarg = 'username' 

    def get_context_data(self, **kwargs):
        context = super(ListUserFollowing, self).get_context_data(**kwargs)
        following = self.object.from2To.all()
        context.update({'following': following})
        return context


#para listar las subscripciones a stories de un usuario
class ListStoriesSubscription(LoginRequiredMixin, generic.DetailView):
    template_name = 'publications/story/story_subscription.html'
    model = CustomUser
    slug_field = 'username'
    slug_url_kwarg = 'username' 

    def get_context_data(self, **kwargs):
        context = super(ListStoriesSubscription, self).get_context_data(**kwargs)
        pub_sub = self.object.pub_subscription.filter(active=True)
        context.update({'list_pub': pub_sub})
        return context

#agregar seguidor a user.
class FollowUser(LoginRequiredMixin, generic.DetailView):
    model = CustomUser
    slug_field = 'username'
    slug_url_kwarg = 'username' 

    def get(self, request, username, id):
        self.request.user.user_subscription.add(self.get_object());
        return redirect(request.GET.get('next'))#agregar seguidor a user.

#unfollow user
class UnfollowUser(LoginRequiredMixin, generic.DetailView):
    model = CustomUser
    slug_field = 'username'
    slug_url_kwarg = 'username' 

    def get(self, request, username, id):
        self.request.user.user_subscription.remove(self.get_object());
        return redirect(request.GET.get('next'))

#para dar de alta un usuario
class SignUpView(generic.CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        form2 = AuthenticationForm()
        context.update({'loginform': form2})
        return context


    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y 
        usamos authenticate para que el usuario incie sesión luego de haberse registrado y 
        lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')

#Eliminar usuario. No se eliminan, se ponen inactivos
class DeleteUser(LoginRequiredMixin, generic.DeleteView):
    def get(self, request, username, id):
        user = CustomUser.objects.get(id=request.user.id)
        userDel = CustomUser.objects.get(id=id)
        if (userDel == user):
            user.is_active=False
            user.save(update_fields=['is_active'])

        return redirect(request.GET.get('logout')) 

#buscar un usuario
class SearchUser(LoginRequiredMixin, generic.DetailView):

    def get(self, *args, **kwargs):
        if (self.request.is_ajax()):
            users = CustomUser.objects.filter(username__icontains=self.kwargs.get('suser'))[:5]
            us = []
            res_users = dict()
            for x in users:
                user = {}
                user.update({'username': x.username})
                user.update({'url': reverse('user:user_profile', kwargs={'username': x.username})})
                us.append(user)
            res_users.update({'users_found': us})
            return JsonResponse(res_users)
