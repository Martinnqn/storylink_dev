from django import forms

class CustomImageField(forms.widgets.ClearableFileInput):
    template_name = 'widgets/custom_image_field.html'
    input_text = 'Cambiar imagen'
    def __init__(self, *args, **kwargs):
        super(CustomImageField, self).__init__(*args, **kwargs)