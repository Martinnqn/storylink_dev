from django.forms import ModelForm
from django import forms
from .models import StoryPublication, ResourcePublication, StoryChapter, Permission
from django_bleach.forms import BleachField
from django.forms import ValidationError
from .widgets import CustomColorSelect, CustomPermissionSelect
from apps.users.widgets import CustomImageField

CHOICES = (
    ('#4a4a4a', '<span style="background:#4a4a4a;" class="palette-color-pub"></span>'),
    ('#314455', '<span style="background:#314455;" class="palette-color-pub"></span>'),
    ('#8f6b99', '<span style="background:#8f6b99;" class="palette-color-pub"></span>'),
    ('#66978e', '<span style="background:#66978e;" class="palette-color-pub"></span>'),
    ('#89abe8', '<span style="background:#89abe8;" class="palette-color-pub"></span>'),
    ('#885930', '<span style="background:#885930;" class="palette-color-pub"></span>'),
    ('#ff6567', '<span style="background:#ff6567;" class="palette-color-pub"></span>'),
    ('#ccb270', '<span style="background:#ccb270;" class="palette-color-pub"></span>'),
    ('#bcd28f', '<span style="background:#bcd28f;" class="palette-color-pub"></span>'),
    ('#e3d2b2', '<span style="background:#e3d2b2;" class="palette-color-pub"></span>'),
    )

'''Nota para saber: agregar el field tag en la definicion de la clase, permite obtener un campo
llamado tag con id = id_tag, pero que no esta asociado al campo tag del modelo. Esto para
evitar que falle form.is_valid() en la view, ya que el field tag del modelo comprueba que cada tag
pertenezca a la relacion tag para poder asociarlo a la StoryPublication. En este caso no hacemos eso
porque los tag que recibimos son strings.'''
class StoryCreationForm(ModelForm):
    tag = forms.CharField(label='Tags', widget=forms.TextInput(), max_length= 80) 
    class Meta:
        model = StoryPublication
        fields = ('title', 'text_content', 'img_content_link', 'color', 'status')
        error_css_class = 'error'
        widgets = {
        'status': CustomPermissionSelect
        }

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Título"
        self.fields['title'].max_length= 120
        self.fields['text_content'] = BleachField()
        self.fields['text_content'].label = "Storylink"
        self.fields['tag'].help_text='''Los tags ayudan a los lectores a encontrar las Storylinks de su interés.
         Puedes probar con ficcion, terror, storyAventura, cienciaFiccion, storyLove, storyKid, etc.
         Los tags se separan con espacios, y pueden tener máximo 80 caracteres.'''
        self.fields['img_content_link'].label = "Agregar Portada"
        self.fields['img_content_link'].validators.append(validate_image)
        self.fields['img_content_link'].help_text = "Los formatos permitidos son jpg, jpeg y png, con un tamaño máximo de 5MB."
        self.fields['color'] = forms.ChoiceField(choices=CHOICES, widget= CustomColorSelect())
        self.fields['color'].initial = '#4a4a4a'
        self.fields['color'].help_text = "Puedes seleccionar un color para personalizar la publicación."
        self.fields['status'].label = "Elige qué acción pueden realizar otros usuarios"
        self.fields['status'].help_text = '''Elige cómo es la visibilidad y qué acciones pueden realizar otros 
                                            usuarios sobre esta publicación. <ul><li>La opción "Leer y Continuar" no podrá
                                            modificarse una vez creada la publicación.</li> <li>La opción "Solo leer" podrá cambiar a "Leer y Escribir"
                                            cuando lo desees.</li> <li>La opción "No leer" podrá cambiarse por cualquiera de las otras opciones.</li></ul>'''

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
         Puedes probar con ficcion, terror, storyAventura, cienciaFiccion, storyLove, storyKid, etc.
         Los tags se separan con espacios y pueden tener máximo 80 caracteres.'''
        self.fields['quest_answ'].label = "Pregunta decisiva para el lector"
        self.fields['quest_answ'].help_text='''La Pregunta Decisiva ayuda al lector a identificar cómo continúa la trama en esta Storylink.
         También puede cumplir el rol de subtítulo.'''

class StoryEditForm(ModelForm):
    tag = forms.CharField(label='Tags', widget=forms.TextInput(), max_length= 80)
    class Meta:
        model = StoryPublication
        fields = ('title', 'text_content', 'img_content_link', 'color', 'status')
        error_css_class = 'error'
        widgets = {
        'img_content_link': CustomImageField,
        'status': CustomPermissionSelect
        }

    def __init__(self, *args, **kwargs):
        super(StoryEditForm, self).__init__(*args, **kwargs)
        self.fields['img_content_link'].label= 'Portada actual'
        self.fields['img_content_link'].required = False
        self.fields['img_content_link'].validators.append(validate_image)
        self.fields['img_content_link'].help_text = "Los formatos permitidos son jpg, jpeg y png, con un tamaño máximo de 5MB."
        self.fields['color'] = forms.ChoiceField(choices=CHOICES, widget= CustomColorSelect()) 
        fpub = kwargs.get('instance', None);
        if (fpub):
            self.initial['tag'] = " ".join([t.tag for t in fpub.tag.all()])
            self.fields['status'].label = "Elige qué acción pueden realizar otros usuarios"
            if (fpub.status==Permission.WR):
                self.fields['status'].disabled = True
                self.fields['status'].help_text = "<span class='material-icons'>error_outline</span> No se pueden cambiar los permisos de esta publicación."
            elif(fpub.status==Permission.R):
                self.fields['status'].help_text = '''Otros usuarios solo pueden leer esta publicación. 
                                            Para que otros usuarios puedan continuar la trama, selecciona la opción "Leer y Continuar".
                                            Las publicaciones con la opción "Leer y Continuar" no pueden cambiarse.'''
            else:
                self.fields['status'].help_text = '''Solo tú puedes ver esta publicación. 
                                            <ul><li>Para que otros usuarios puedan continuar la trama, selecciona la opción "Leer y Continuar".
                                            Las publicaciones con la opción "Leer y Continuar" no pueden cambiarse.</li>
                                            <li>Para que otros usuarios puedan leer esta publicación, selecciona la opción "Solo leer". 
                                            La opción "Solo leer" puede cambiarse a "Leer y Continuar".</li>
                                            <li>Las publicaciones no pueden volver al estado "No ver".</li>
                                            </ul>'''
        self.fields['text_content'] = BleachField()
        self.fields['text_content'].label = "Story"
        self.fields['title'].label = "Título"
        self.fields['title'].max_length= 120

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
        self.fields['title'].label = "Título"
        self.fields['title'].required = False
        self.fields['tag'].required = False



def validate_image(image):
    filesize = image.size
    megabyte_limit = 5.0
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError("El tamaño máximo permitido para las imágenes es %sMB" % str(megabyte_limit))