from django import forms
from django.forms import ValidationError, ModelForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, UserProfile
import re
from django.contrib.auth.forms import AuthenticationForm
from .widgets import CustomImageField
from social_django.models import UserSocialAuth

# permite usuarios inactivos ser autenticados. no significa que les permita loguearse.


class AuthenticationFormWithInactiveUsersOkay(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if (not user.email_verified):
            raise forms.ValidationError(
                _('El correo electrónico de esta cuenta no se ha verificado. Por favor revise su correo electrónico y acceda al ' +
                    'enlace enviado para verificar que usted es el propietario del correo.'),
                code='email_not_verified',
            )


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name',)
        error_css_class = 'error'

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Nombre de usuario"
        self.fields['username'].help_text = 'El nombre de usuario puede contener letras, números, guiones, puntos y @.'
        self.fields['first_name'] = forms.CharField(required=True)
        self.fields['first_name'].label = "Nombre"
        self.fields['first_name'].validators.append(only_chars)
        self.fields['last_name'] = forms.CharField(required=True)
        self.fields['last_name'].label = "Apellido"
        self.fields['last_name'].validators.append(only_chars)


class CreateUserProfile(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('link_img_perfil', 'description')
        error_css_class = 'error'

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['link_img_perfil'].label = "Imagen de perfil"
        self.fields['description'].label = "Cuéntanos sobre ti"
        self.fields['description'].help_text = "150 caracteres como máximo"

# para el nombre y apellido solo letras y espacios.


def only_chars(value):
    regex = re.compile('[a-zA-ZáéíóúÁÉÍÓÚ\s]+$')
    if (not regex.match(value)):
        raise ValidationError(
            _('Solo se permiten letras.'),
            params={'value': value},
        )


class MailCheck(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email',)
        error_css_class = 'error'


class UsernameCheck(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username',)
        error_css_class = 'error'


class EditAccount(ModelForm):
    class Meta():
        model = CustomUser
        # por ahora el email y la contrasenia no se pueden editar.
        fields = ('username', 'first_name', 'last_name',)
        error_css_class = 'error'

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Nombre de usuario"
        self.fields['username'].help_text = 'El nombre de usuario puede contener letras, números, guiones, puntos y @.'
        self.fields['first_name'] = forms.CharField(required=True)
        self.fields['first_name'].label = "Nombre"
        self.fields['first_name'].validators.append(only_chars)
        self.fields['last_name'] = forms.CharField(required=True)
        self.fields['last_name'].label = "Apellido"
        self.fields['last_name'].validators.append(only_chars)
        if (kwargs.get('instance', None)):
            if(UserSocialAuth.objects.filter(user=kwargs.get('instance')).exists()):
                self.fields['first_name'].disabled = True
                self.fields['last_name'].disabled = True


class EditUserProfile(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('link_img_perfil', 'description')
        error_css_class = 'error'
        widgets = {
            'link_img_perfil': CustomImageField
        }

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['link_img_perfil'].label = "Imagen de perfil"
        self.fields['description'].label = "Cuéntanos sobre ti"
        self.fields['description'].help_text = "150 caracteres como máximo"
