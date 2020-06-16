from storylink_dev.celery import app
from django.core import mail

from django.db import transaction, IntegrityError
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.template.loader import render_to_string
from django.core.mail import get_connection
from django.urls import reverse_lazy
from apps.users.models import UserProfile
from .token import account_activation_token

from django.db.models import Q

@app.task
def createBulkMail(header, content, category, to, current_site):
    '''Actualmente se crean todos los emails y luego se envian a send_messages para que se envien 
    asincronamente. Sin embargo es ineficiente crearlos todos de una porque estan todos en memoria.
    Buscar la forma de crear subconjuntos de emails, enviarlos y esperar a que se envien todos para
    crear nuevos subconjuntos. VER celery.result y asyncresult'''
    recipients = getRecipients(category, to)
    #print(recipients)
    emails = []
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
        emailmsg = mail.EmailMessage(header,message, to=[email])
        emailmsg.content_subtype = "html"
        emails.append(emailmsg)
    con = get_connection()
    con.open()
    con.send_messages(emails)
    con.close()

'''retorna la lista de usuarios a quienes se le enviara el mail. to='0' representa a los admins,
to='1' representa a usuarios sin admins y to='2' representa a todos usuarios+admins.'''
def getRecipients(category, to):
    cat = Q(cat_unsubscribed__id=category)
    if (to=='1'):
        rec = UserProfile.objects.filter(user__is_staff=False).filter(~cat).values_list('id', 'user__username', 'user__email')
        return rec
    elif (to=='2'):
        rec = UserProfile.objects.filter(~cat).values_list('id', 'user__username', 'user__email')
        return rec
    elif (to=='0'):
        rec = UserProfile.objects.filter(user__is_staff=True).filter(~cat).values_list('id', 'user__username', 'user__email')
        return rec