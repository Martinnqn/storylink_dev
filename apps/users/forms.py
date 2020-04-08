from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'link_img_perfil', 'description')
        error_css_class = 'error'
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['link_img_perfil'].label = "Imagen de perfil"
        self.fields['username'].label = "Nombre de usuario"
        self.fields['first_name']= forms.CharField(required = True) 
        self.fields['first_name'].label= "Nombre"
        self.fields['last_name']= forms.CharField(required = True) 
        self.fields['last_name'].label= "Apellido"
        self.fields['description'].label= "Cuéntanos sobre ti"
