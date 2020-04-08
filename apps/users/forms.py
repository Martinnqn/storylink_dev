from django import forms
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'link_img_perfil', 'description')
        error_css_class = 'error'
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['link_img_perfil'].label = "Imagen de perfil"
        self.fields['username'].label = "Nombre de usuario"
        self.fields['username'].validators.append(unique_user)
        self.fields['first_name']= forms.CharField(required = True) 
        self.fields['first_name'].label= "Nombre"
        self.fields['last_name']= forms.CharField(required = True) 
        self.fields['last_name'].label= "Apellido"
        self.fields['description'].label= "Cuéntanos sobre ti"


#validar si el usuario es unico y no contiene punto
def unique_user(value):
    if('.' in value):
        raise ValidationError(
            _('No se permiten utilizar puntos "." en los nombres de usuario.'),
            params={'value': value},
        )
    exist = CustomUser.objects.filter(username__iexact=value).exists()
    if (exist):
        raise ValidationError(
            _('El nombre de usuario "%(value)s" ya está en uso.'),
            params={'value': value},
        )