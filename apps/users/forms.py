from django import forms
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
import re

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'link_img_perfil', 'description')
        error_css_class = 'error'
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['link_img_perfil'].label = "Imagen de perfil"
        self.fields['username'].label = "Nombre de usuario"
        self.fields['username'].help_text='El nombre de usuario puede contener letras, números, guiones, puntos y @.'
        self.fields['first_name']= forms.CharField(required = True) 
        self.fields['first_name'].label= "Nombre"
        self.fields['first_name'].validators.append(only_chars)
        self.fields['last_name']= forms.CharField(required = True) 
        self.fields['last_name'].label= "Apellido"
        self.fields['last_name'].validators.append(only_chars)
        self.fields['description'].label= "Cuéntanos sobre ti"
        self.fields['description'].help_text = "150 caracteres como máximo"

#para el nombre y apellido solo letras y espacios.
def only_chars(value):
    regex = re.compile('[a-zA-ZáéíóúÁÉÍÓÚ\s]+$')
    if (not regex.match(value)):
        raise ValidationError(
            _('Solo se permiten letras.'),
            params={'value': value},
        )


class MailCheck(forms.Form):
    class Meta:
        model = CustomUser
        fields = ('email')
        error_css_class = 'error'

class UsernameCheck(forms.Form):
    class Meta:
        model = CustomUser
        fields = ('username')
        error_css_class = 'error'