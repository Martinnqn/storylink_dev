from django.core.mail import EmailMessage
from storylink_dev.celery import app
from django.template.loader import render_to_string
from .token import account_activation_token
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


@app.task
def send_mail_confirm(userid, username, email, domain):
    mail_subject = 'Registro de usuario.'
    message = render_to_string('registration/activate_account.html', {
        'username': username,
        'domain': domain,
        'uid': urlsafe_base64_encode(force_bytes(userid)),
        'token': account_activation_token.make_token(userid),
    })
    email = EmailMessage(mail_subject, message, to=[email])
    email.content_subtype = "html"
    email.send()
