from django.forms import ModelForm
from django import forms
from .models import Category

CHOICES = (
    ('0', 'admins'),
    ('1', 'users'),
    ('2', 'all'),
    )

class MassiveEmailForm(forms.Form):
    headerMail = forms.CharField(label='Mail header', widget=forms.TextInput(), max_length= 80)
    contentMail = forms.CharField(label='Mail content', widget=forms.Textarea, max_length= 2000)
    category = forms.ChoiceField(choices=([['','-------------']] + list(Category.objects.all().values_list('id', 'name'))))
    to = forms.ChoiceField(choices=CHOICES, widget= forms.widgets.RadioSelect())
