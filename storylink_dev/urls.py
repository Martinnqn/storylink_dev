"""storylink_dev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.views.generic.base import TemplateView
from apps.users.views import SignUpView, mail_check, username_check, FillProfile, VerifiedMail, CustomLoginView
from apps.users.views import ReactV
from apps.publications.views import ListStories


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('success/<success>', CustomLoginView.as_view(),
         name='hall_s'),  # pagina principal
    path('activated/<activated>', ListStories.as_view(),
         name='hall_a'),  # pagina principal
    path('', ListStories.as_view(), name='hall'),  # pagina principal
    path('admin/site/', admin.site.urls),
    # matchea con un string despues del .com/ y termina de procesarlo en el archivo urls de users
    path('user/<str:username>/', include('apps.users.urls')),
    # para iniciar sesion con el formulario que permite usuarios inactivos
    path('accounts/login/', CustomLoginView.as_view(), name="custom_login"),
    # para la administracion de la cuenta de usuario
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='sign_up'),
    path('terminos_privacidad/',
         TemplateView.as_view(template_name='term_priv.html'),  name='term_priv'),
    path('social/', include('social_django.urls', namespace='social')),
    path('re_email/', mail_check.as_view(), name='form_new_mail'),
    path('re_username/', username_check.as_view(), name='form_new_username'),
    path('fillprofile/<uidb64>/', FillProfile.as_view(), name='fill_profile'),
    path('fillprofile/<uidb64>/<email_verified>',
         FillProfile.as_view(), name='fill_profile'),
    path('activate/<uidb64>/<token>', VerifiedMail.as_view(), name='activate'),
    path('test', ReactV.as_view(), name='activate'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
