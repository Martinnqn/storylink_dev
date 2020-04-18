from social_core.pipeline.partial import partial
from django import forms
from .models import CustomUser, unique_user
from django.shortcuts import render_to_response
from django.forms import ValidationError

from django.http import HttpResponseRedirect
import urllib

def setPicture(backend, strategy, details, response, user=None, *args, **kwargs):
    if (user):
        print(user)
        print(response.get('picture').get('data').get('url'))
        user.link_img_perfil = response.get('picture').get('data').get('url')
        user.save()

@partial
def require_email(strategy, details, user=None, is_new=False, *args, **kwargs):
    if kwargs.get('ajax') or user and user.email:
        return
    elif is_new and not details.get('email'):
        email = strategy.request_data().get('email')
        if email:
            details['email'] = email
        else:
            current_partial = kwargs.get('current_partial')
            return render_to_response('registration/force_get_email.html')

@partial
def check_unique_username(strategy, details, user=None, is_new=False, *args, **kwargs):
    if user and user.username:
        return
    if (details['username']):
        cusername = details['username'].replace(" ", "")
        storage = strategy.storage
        exist = True
        try:
            unique_user(cusername)
        except ValidationError as e:
           
