from django import forms

class CustomColorSelect(forms.widgets.RadioSelect):
    template_name = 'widgets/select_color.html'
    input_text = 'color'
    def __init__(self, *args, **kwargs):
        super(CustomColorSelect, self).__init__(*args, **kwargs)