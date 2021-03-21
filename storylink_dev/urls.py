from django.contrib import admin
from django.urls import path, include

from django.views.generic.base import TemplateView
from apps.users.views import SignUpView, mail_check, username_check, \
    FillProfile, VerifiedMail, CustomLoginView, SignUpApiConnectorView

from apps.users.api.views import UserViewSet, UserProfileViewSet, \
    FullUserDataViewSet, WhoamiViewSet

from apps.publications.api.views import StoryPublicationViewSet, \
    StoryChapterViewSet

from apps.users.views import ReactV, B2CViewSet, UserMigration
from apps.publications.views import ListStories


from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
# import routers
from rest_framework import routers

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register('users', UserViewSet)
router.register('profiles', UserProfileViewSet)
router.register('full-users', FullUserDataViewSet)
router.register('stories', StoryPublicationViewSet)
router.register('chapters', StoryChapterViewSet)
router.register('whoami', WhoamiViewSet, basename='whoami')

API_VERSION = 1

api_urls = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include(router.urls)),
]

urlpatterns = [
    path('success/<success>', CustomLoginView.as_view(),
         name='hall_s'),  # pagina principal
    path('activated/<activated>', ListStories.as_view(),
         name='hall_a'),  # pagina principal
    path('', ListStories.as_view(), name='hall'),  # pagina principal
    path('admin/site/', admin.site.urls),
    # matchea con un string despues del .com/ y termina de procesarlo en el archivo urls de users
    path('users/<str:username>/', include('apps.users.urls')),
    path('migrate/<suser>', UserMigration.as_view(), name='user_migrate'),
    # para iniciar sesion con el formulario que permite usuarios inactivos
    path('accounts/login/', CustomLoginView.as_view(), name="custom_login"),
    # para la administracion de la cuenta de usuario
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='sign_up'),
    path('signup-connector/', SignUpApiConnectorView.as_view(), name='sign_up_connector'),
    path('terminos_privacidad/',
         TemplateView.as_view(template_name='term_priv.html'),  name='term_priv'),
    path('social/', include('social_django.urls', namespace='social')),
    path('re_email/', mail_check.as_view(), name='form_new_mail'),
    path('re_username/', username_check.as_view(), name='form_new_username'),
    path('fillprofile/<uidb64>/', FillProfile.as_view(), name='fill_profile'),
    path('fillprofile/<uidb64>/<email_verified>',
         FillProfile.as_view(), name='fill_profile'),
    path('activate/<uidb64>/<token>', VerifiedMail.as_view(), name='activate'),
    path('api/v%d/b2c' % (API_VERSION), B2CViewSet.as_view(), name='b2c'),
    path('api/v%d/' % (API_VERSION), include(api_urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
