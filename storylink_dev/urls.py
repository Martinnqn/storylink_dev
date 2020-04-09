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
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from apps.users.views import SignUpView
from apps.publications.views import ListStories

from django.contrib.auth.decorators import login_required, permission_required

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', TemplateView.as_view(template_name='hall/hall.html'), name='hall'), # pagina principal
    path('', ListStories.as_view(), name='hall'), # pagina principal
    path('admin/site/', admin.site.urls),
    path('user/<str:username>/', include('apps.users.urls')), #matchea con un string despues del .com/ y termina de procesarlo en el archivo urls de users
    path('accounts/', include('django.contrib.auth.urls')), # para la administracion de la cuenta de usuario
    path('signup/', SignUpView.as_view(), name='sign_up'), 
    path('terminos_privacidad/', TemplateView.as_view(template_name='term_priv.html'),  name='term_priv'),   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)