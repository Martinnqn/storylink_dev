from social_core.pipeline.partial import partial
from django import forms
from .models import CustomUser, check_characters, UserProfile
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.forms import ValidationError
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from urllib.request import urlopen, HTTPError
from django.core.files.base import ContentFile

def setPicture(backend, strategy, details, response, user=None, *args, **kwargs):
    if (user):
        print(user)
        print(response.get('picture').get('data').get('url'))
        user.link_img_perfil = response.get('picture').get('data').get('url')
        user.save()

@partial
def require_email(backend, strategy, details, user=None, is_new=False, *args, **kwargs):
    if user and user.email:
        return
    elif is_new and not details.get('email'):
        #email = strategy.request_data().get('email')
        email = strategy.session_get('email', None)
        if email:
            exist = CustomUser.objects.filter(email__iexact=email).exists()
            if (exist):
                current_partial = kwargs.get('current_partial')
                return strategy.redirect(
                '/re_email?partial_token={0}&used=True'.format(current_partial.token)
                )
            else:
                details['email'] = email
        else:
            current_partial = kwargs.get('current_partial')
            return strategy.redirect(
                '/re_email?partial_token={0}'.format(current_partial.token)
            )
    elif is_new and details.get('email'):
        if (strategy.session_get('email', None)):
            exist = CustomUser.objects.filter(email__iexact=strategy.session_get('email')).exists()
            if (exist):
                current_partial = kwargs.get('current_partial')
                return strategy.redirect(
                '/re_email?partial_token={0}&used=True'.format(current_partial.token)
                )
            else:
                details['email'] = strategy.session_get('email')
        else:
            exist = CustomUser.objects.filter(email__iexact=details.get('email')).exists()
            if (exist):
                current_partial = kwargs.get('current_partial')
                return strategy.redirect(
                '/re_email?partial_token={0}&used=True'.format(current_partial.token)
                )
                
@partial
def get_username(backend, strategy, details, user=None, is_new=False, *args, **kwargs):
    if user and user.username:
        return
    elif strategy.session_get('username'):
        new_username = strategy.session_get('username')
    elif details.get('username'):
            new_username = details.get('username').replace(" ", ".")
    else:
        if (details.get('first_name') and details.get('last_name')):
            new_username = details.get('first_name')+'.'+details.get('last_name')
        else:
            new_username = 'username'

    if new_username:
        exist = CustomUser.objects.filter(username__iexact=new_username).exists()
        if (exist):
            current_partial = kwargs.get('current_partial')
            return strategy.redirect(
            '/re_username?partial_token={0}&used=True'.format(current_partial.token)
            )
    return {'username': new_username}

@partial
def check_unique_username(backend, strategy, details, user=None, is_new=False, *args, **kwargs):
    if user and user.username:
        return
    elif strategy.session_get('username'):
        new_username = strategy.session_get('username')
    elif kwargs.get('username'):
        new_username = kwargs.get('username')
    if new_username:
        exist = CustomUser.objects.filter(username__iexact=new_username).exists()
        if (exist):
            current_partial = kwargs.get('current_partial')
            print("denuevo")
            return strategy.redirect(
            '/re_username?partial_token={0}&used=True'.format(current_partial.token)
            )
        else:
            print("ahorasi")
            print(new_username)
            details['username'] = new_username
            kwargs.update({'username': new_username})
    else:
        print("elelse")        
        current_partial = kwargs.get('current_partial')
        return strategy.redirect(
            '/re_username?partial_token={0}'.format(current_partial.token)
        )
'''@partial
def check_unique_username(backend, strategy, details, user=None, is_new=False, *args, **kwargs):
    if user and user.username:
        return
    elif is_new and not details.get('username'):
        username = strategy.session_get('username', None)
        if username:
            exist = CustomUser.objects.filter(username__iexact=username).exists()
            if (exist):
                current_partial = kwargs.get('current_partial')
                return strategy.redirect(
                '/re_username?partial_token={0}&used=True'.format(current_partial.token)
                )
            else:
                return {'username': username}
        else:
            current_partial = kwargs.get('current_partial')
            return strategy.redirect(
                '/re_username?partial_token={0}'.format(current_partial.token)
            )
    elif is_new and details.get('username'):
        if (strategy.session_get('username', None)):
            exist = CustomUser.objects.filter(username__iexact=strategy.session_get('username')).exists()
            if (exist):
                current_partial = kwargs.get('current_partial')
                return strategy.redirect(
                '/re_username?partial_token={0}&used=True'.format(current_partial.token)
                )
            else:
                return {'username': strategy.session_get('username')}
        else:
            exist = CustomUser.objects.filter(username__iexact=details.get('username')).exists()
            if (exist):
                current_partial = kwargs.get('current_partial')
                return strategy.redirect(
                '/re_username?partial_token={0}&used=True'.format(current_partial.token)
                )
'''

#lo usaba antes de social_core.pipeline.social_auth.social_user porque lanzaba error twitter AuthAlreadyAssociated
def userExist(backend, strategy, details, response, user=None, *args, **kwargs):
    if (user):
        print(user)
        return redirect(reverse_lazy('hall'))


#Si el usuario es nuevo crea un Profile, sino actualiza los datos del profile con los del provider (actualmente solo la imagen de perfil). Asi, si un usuario actualiza
#un dato en el provider, tambien se actualiza en su perfil cuando inicia sesion.
def update_or_create_userProfile(backend, strategy, details, response, user=None, *args, **kwargs):
    if (user and kwargs.get('is_new')):
        if (backend.name == "twitter"):
            profile = UserProfile(user=user)
            saveImage(response.get('profile_image_url_https'), profile, user.id)
            profile.save()
        elif (backend.name == "facebook"):
            profile = UserProfile(user=user)
            saveImage(response.get('picture')['data']['url'], profile, user.id)
            profile.save()
        user.email_verified = True
        user.save()
    elif (user and not kwargs.get('is_new')):
        if (backend.name == "twitter"):
            profile = user.profile.get()
            saveImage(response.get('profile_image_url_https'), profile, user.id)
            profile.save()
        elif (backend.name == "facebook"):
            profile = user.profile.get()
            saveImage(response.get('picture')['data']['url'], profile, user.id)
            profile.save()


def saveImage(url, profile, id):
    img = urlopen(url)
    profile.link_img_perfil.save(str(id) + '.jpg', ContentFile(img.read()))


def get_avatar_url(request, backend, response,  user=None, *args, **kwargs):
    """Pipeline to get user avatar from Twitter/FB via django-social-auth"""
    avatar_url = ''
    if (user):
        if (backend.name == "twitter"):
            avatar_url = response.get('profile_image_url', '')
            print("ENCONTRO IMAGEN")
            print(avatar_url)
            print(user)
            #aca deberia guardar la imagen en el user.