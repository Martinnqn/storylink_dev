from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

#from apps.publications.models import StoryPublication #import circular! solucionado con app_level.ModelName (publications.StoryPublication)

# Create your models here.

# usuario
class CustomUser(AbstractUser):
    link_img_perfil = models.ImageField(upload_to = 'gallery/profiles', default = 'gallery/no-img-profile.png')
    description = models.CharField(max_length=150, blank=True)
    username = models.CharField(unique=True, max_length=20)
    email = models.EmailField(unique=True)
    # a que usuario esta suscripto. Se usa un modelo intermedio para especificar los atributos de la tabla intermedia.
    user_subscription = models.ManyToManyField('self', through='UserSubscriptionModelAux', symmetrical=False)
    # a que publicacion esta suscripto. Se usa un modelo intermedio para especificar los atributos de la tabla intermedia.
    pub_subscription = models.ManyToManyField('publications.StoryPublication', through='PubSubscriptionModelAux', symmetrical=False)
    # si el usuario tiene la cuenta reportada
    is_reported = models.BooleanField(default=False)
    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS =['username'] 
    def __str__(self):
        return self.username

# modelo intermedio para las suscripciones de un usuario a otro usuario. from_user esta suscripto a to_user
class UserSubscriptionModelAux(models.Model):
    date_time = models.DateField(auto_now_add=True)
    from_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='from2To')
    to_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='to2From')


# modelo intermedio para las suscripciones de un usuario a publicaciones.
class PubSubscriptionModelAux(models.Model):
    date_time = models.DateField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user2Pub')
    pub = models.ForeignKey('publications.StoryPublication', on_delete=models.CASCADE, related_name='pub2User')


# modelo para el registro de acciones del usuario.
class UserEvents(models.Model):
    date_time = models.DateField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=5)
    id_publication = models.IntegerField()


