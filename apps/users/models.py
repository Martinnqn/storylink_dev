from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
import re
from django.contrib.auth.models import UserManager


def unique_user(value):
    """funcion para validar si el usuario es unico (equalsIgnoreCase) y no contiene punto."""

   if (not check_characters(value)):
        raise ValidationError(
            _('No se permiten utilizar caracteres especiales como ", ?,¡, &, %%, ., comas, espacios, etc en los nombres de usuario.'),
            params={'value': value},
        )
    '''exist = CustomUser.objects.filter(username__iexact=value).exists()
    if (exist):
        raise ValidationError(
            _('El nombre de usuario "%(value)s" ya está en uso.'),
            params={'value': value},
        )'''


def check_characters(value):
    regex = re.compile('[.@\w]+$')
    return regex.match(value)


def get_upload_path(instance, filename):
    return 'users/user_{0}/{1}'.format(instance.user.id, filename)


class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(
            self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})



class CustomUser(AbstractUser):
    # User representation in the app

    objects = CustomUserManager()
    username = models.CharField(
        'Nombre de usuario', unique=True, max_length=35, validators=[unique_user])
    email = models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS =['username']

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    """User Profile is separated from user representation.
    This model has specific data of user in Storylink"""

    user = models.ForeignKey(
        CustomUser, related_name='profile', on_delete=models.PROTECT)
    link_img_perfil = models.ImageField(
        upload_to=get_upload_path, default='gallery/no-img-profile.png', max_length=350)
    description = models.CharField(max_length=150, blank=True)
    # a que usuario esta suscripto. Se usa un modelo intermedio para especificar los atributos de la tabla intermedia.
    user_subscription = models.ManyToManyField(
        'self', through='UserSubscriptionModelAux', symmetrical=False)
    # a que publicacion esta suscripto. Se usa un modelo intermedio para especificar los atributos de la tabla intermedia.
    pub_subscription = models.ManyToManyField(
        'publications.StoryPublication', through='PubSubscriptionModelAux', symmetrical=False)
    # si el usuario tiene la cuenta reportada
    is_reported = models.BooleanField(default=False)



class UserSubscriptionModelAux(models.Model):
    """Intermediate model for subscription from user to other user. 
    from_user is subscripted to to_user"""

    date_time = models.DateField(auto_now_add=True)
    from_user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='from2To')
    to_user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='to2From')


class PubSubscriptionModelAux(models.Model):
    """Intermediate model for subscription from user to publications. 
    user is subscripted to pub"""

    date_time = models.DateField(auto_now_add=True)
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='user2Pub')
    pub = models.ForeignKey('publications.StoryPublication',
                            on_delete=models.CASCADE, related_name='pub2User')


class UserEvents(models.Model):
    """Modelo para el registro de acciones del usuario."""
    
    date_time = models.DateField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=5)
    id_publication = models.IntegerField()
