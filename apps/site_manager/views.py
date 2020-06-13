from django.shortcuts import render

from django.db import transaction, IntegrityError
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.template.loader import render_to_string
from django.core.mail import send_mass_mail, get_connection
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic, View
from apps.users.models import CustomUser
from .token import account_activation_token
from django.contrib.sites.shortcuts import get_current_site

from .models import UnsubscribeMassiveMail
from .forms import MassiveEmailForm



class SendMassiveEmail(LoginRequiredMixin, generic.edit.FormView):
    form_class = MassiveEmailForm
    template_name = 'site_manager/massive_mail.html'

    def __init__(self, from_email=None):
        # TODO setup the default from email
        self.connection = get_connection()
        self.from_email = from_email

    def form_valid(self, form):
        header = self.request.POST['headerMail']
        content = self.request.POST['contentMail']
        category = self.request.POST['category']
        to = self.request.POST['to']
        if self.request.user.is_staff:
            recipients = getRecipients(category, to)
            #print(recipients)
            current_site = get_current_site(self.request)
            for userid, user, email in recipients:
                uid = urlsafe_base64_encode(force_bytes(userid))
                uidcat = urlsafe_base64_encode(force_bytes(category))
                token = account_activation_token.make_token(userid)
                message = render_to_string('site_manager/mail_structure.html', {
                    'content': content,
                    'username': user,
                    'domain': current_site,
                    'urlUnsubscribe': reverse_lazy('site_manager:unsubscribe', kwargs={'uidb64': uid, 'uidb64cat': uidcat,'token': token}),
                })
                msgs = (header, message, email)
                self.__send_mail(msgs)
                #print(content)
                #print(msg)
                #send_mass_mail((msg), fail_silently=False)
        else:
            return redirect('/')

    from django_celery_tutorial.celery import app
    @app.task
    def __send_mail(self, messages):
        self.connection.open()
        self.connection.send_messages(messages)
        self.connection.close()

'''retorna la lista de usuarios a quienes se le enviara el mail. to='0' representa a los admins,
to='1' representa a usuarios sin admins y to='2' representa a todos usuarios+admins.'''
def getRecipients(category, to):
    if (to=='1'):
        ex = UnsubscribeMassiveMail.objects.filter(category = category).values_list('user__id', 'user__username', 'user__email')
        print(ex)
        rec = CustomUser.objects.filter(is_staff=False).values_list('id', 'username', 'email').difference(ex)
        return rec
    elif (to=='2'):
        ex = UnsubscribeMassiveMail.objects.filter(category = category).values_list('user__id', 'user__username', 'user__email')
        print(ex)
        rec = CustomUser.objects.filter().values_list('id', 'username', 'email').difference(ex)
        return rec
    elif (to=='0'):
        rec = CustomUser.objects.filter(is_staff=True).values_list('id', 'username', 'email')
        #rec = CustomUser.objects.filter(is_staff=True)
        return rec

class Unsubscribe(generic.View):
    pass