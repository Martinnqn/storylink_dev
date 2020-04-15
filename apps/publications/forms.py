from django.forms import ModelForm
from django import forms
from .models import StoryPublication, ResourcePublication, StoryChapter
from django.shortcuts import get_object_or_404
from django_bleach.forms import BleachField
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
import bleach
from django.utils.html import conditional_escape, escape

'''Nota para saber: agregar el field tag en la definicion de la clase, permite obtener un campo
llamado tag con id = id_tag, pero que no esta asociado al campo tag del modelo. Esto para
evitar que falle form.is_valid() en la view, ya que el field tag del modelo comprueba que cada tag
pertenezca a la relacion tag para poder asociarlo a la StoryPublication. En este caso no hacemos eso
porque los tag que recibimos son strings.'''
class StoryCreationForm(ModelForm):
    tag = forms.CharField(label='Tags', widget=forms.TextInput(), max_length= 80) 
    class Meta:
        model = StoryPublication
        fields = ('title', 'text_content', 'img_content_link')
        error_css_class = 'error'
    
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Título"
        self.fields['title'].max_length= 120
        self.fields['text_content'] = BleachField()
        self.fields['text_content'].label = "Storylink"
        self.fields['tag'].help_text='''Los tags ayudan a los lectores a encontrar las Storylinks de su interés.
         Puedes probar con "ficcion", "terror", "storyAventura", "cienciaFiccion", "storyLove", "storyKid", etc.
         Los tags se separan con espacios, y pueden tener máximo 80 caracteres.'''
        self.fields['img_content_link'].label = "Agregar Portada"

class StoryContinuationCreationForm(ModelForm):
    tag = forms.CharField(label='Tags', widget=forms.TextInput(), max_length= 80)
    title = forms.CharField(label='Título', widget=forms.HiddenInput())

    class Meta:
        model = StoryChapter
        fields = ('quest_answ', 'text_content')
        error_css_class = 'error'

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        if (kwargs.get('instance', None)):
            self.initial['title'] = kwargs.get('instance').title
        self.initial['text_content'] = ""
        self.fields['text_content'] = BleachField()
        self.fields['text_content'].label = "Story"
        self.fields['tag'].initial = ""
        self.fields['tag'].help_text='''Los tags ayudan a los lectores a encontrar las Storylinks de su interés.
         Puedes probar con "ficcion", "terror", "storyAventura", "cienciaFiccion", "storyLove", "storyKid", etc.
         Los tags se separan con espacios y pueden tener máximo 80 caracteres.'''
        self.fields['quest_answ'].label = "Pregunta decisiva para el lector"
        self.fields['quest_answ'].help_text='''La Pregunta Decisiva ayuda al lector a identificar cómo continúa la trama en esta Storylink.
        Por ejemplo, si el protagonista principal debe decidir entre quedarse en casa o romper la cuarentena, se puede
        continuar la trama con una pregunta: "¿Romper cuarentena?" o "¿#yoMeQuedoEnCasa?". También puede escribirse en
        forma de subtítulo, sin embargo hacerlo en forma de pregunta resulta mas interactivo para el lector.'''

class StoryEditForm(ModelForm):
    tag = forms.CharField(label='Tags', widget=forms.TextInput(), max_length= 80)
    class Meta:
        model = StoryPublication
        fields = ('title', 'text_content', 'img_content_link')
        error_css_class = 'error'

    def __init__(self, *args, **kwargs):
        super(StoryEditForm, self).__init__(*args, **kwargs)
        self.fields['img_content_link'].label= 'Portada actual'
        self.fields['img_content_link'].required = False
        fpub = kwargs.get('instance', None);
        if (fpub):
            self.initial['tag'] = " ".join([t.tag for t in fpub.tag.all()])
        self.fields['text_content'] = BleachField()
        self.fields['text_content'].label = "Story"
        self.fields['title'].label = "Título"
        self.fields['title'].max_length= 120
        #self.fields['img_content_link'].label = "Portada actual"

class StoryChapterEditForm(ModelForm):
    tag = forms.CharField(label='Tags', widget=forms.TextInput(), max_length= 80)
    class Meta:
        model = StoryChapter
        fields = ('quest_answ', 'text_content')
        error_css_class = 'error'

    def __init__(self, *args, **kwargs):
        super(StoryChapterEditForm, self).__init__(*args, **kwargs)
        fpub = kwargs.get('instance', None);
        if (fpub):
            self.initial['tag'] = " ".join([t.tag for t in fpub.tag.all()])
        self.fields['quest_answ'].label = 'Pregunta decisiva para el lector'
        self.fields['text_content'] = BleachField()
        self.fields['text_content'].label = "Story"


#Resources
class ResourceCreationForm(ModelForm):
    class Meta:
        model = ResourcePublication
        fields = ('title', 'text_content', 'privacity', 'tag', 'img_content_link')
        error_css_class = 'error'
    def __init__(self, *args, **kwargs):
        super(ResourceCreationForm, self).__init__(*args, **kwargs)
        self.fields['text_content'].label = "Description"
        self.fields['tag'].label = "Tags"

class ResourceEditForm(ModelForm):
    class Meta:
        model = ResourcePublication
        fields = ('title', 'text_content', 'privacity', 'tag', 'img_content_link')
        error_css_class = 'error'
    def __init__(self, *args, **kwargs):
        super(ResourceEditForm, self).__init__(*args, **kwargs)
        self.fields['text_content'].label = "Description"
        self.fields['tag'].label = "Tags"


class FilterHall(ModelForm):
    tag = forms.CharField(label='Tags', widget=forms.TextInput()) 
    class Meta:
        model = StoryPublication
        fields = ('title',)
        error_css_class = 'error'
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['title'].required = False
        self.fields['tag'].required = False