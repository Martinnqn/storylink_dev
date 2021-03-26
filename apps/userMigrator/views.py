from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic, View
from django.contrib.auth import login, authenticate
from apps.users.models import CustomUser, UserProfile
from django.http import JsonResponse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime, timedelta
from dateutil import tz, parser
from .auth_helper import get_access_token
from .graph_helper import create_user

from django.db import connection


def get_user_for_migrate(username):
    with connection.cursor() as cursor:
        cursor.execute('exec CustomUser_get %s' % username)
        rows = cursor.fetchall()
        passwordConfig = dict()
        passwordConfig.update({'forceChangePasswordNextSignIn': False})
        passwordConfig.update({'password': 'WwvJ]6NMw+bWH-'})
        us = []
        while rows:
            for x in rows:
                user = dict()
                ident = []
                ident.append({
                    'signInType': 'userName',
                    'issuer': 'storylinkB2C.onmicrosoft.com',
                    'issuerAssignedId': x[1]
                })
                ident.append({
                    'signInType': 'emailAddress',
                    'issuer': 'storylinkB2C.onmicrosoft.com',
                    'issuerAssignedId': x[4]
                })
                user.update(
                    {'extension_8fe2c4d0-5118-4a84-a0bc-04a9b8ec6a76_userID': x[0]})
                user.update({'displayName': x[1]})
                user.update({'identities': ident})
                user.update({'passwordProfile': passwordConfig})
                user.update({'passwordPolicies': 'DisablePasswordExpiration'})
                us.append(user)
            if cursor.nextset():
                rows = cursor.fetchall()
            else:
                rows = None
    return us


class UserMigration(generic.DetailView):
    def get(self, *args, **kwargs):
        username = self.kwargs.get('suser')
        user = get_user_for_migrate(username)
        if (user and user[0]):
            access_token = get_access_token()
            print(user[0])
            resp = create_user(access_token, user[0])
            print(resp)
            return JsonResponse(resp)
        return JsonResponse({'error': 'usuario no encontrado'})
