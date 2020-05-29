from django import forms

class CustomColorSelect(forms.widgets.RadioSelect):
    template_name = 'widgets/select_color.html'
    def __init__(self, *args, **kwargs):
        super(CustomColorSelect, self).__init__(*args, **kwargs)

class CustomPermissionSelect(forms.widgets.RadioSelect):
    template_name = 'widgets/select_permission.html'
    def __init__(self, *args, **kwargs):
        super(CustomPermissionSelect, self).__init__(*args, **kwargs)