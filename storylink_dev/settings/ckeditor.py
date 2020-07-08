#configuracion ckeditor 
CKEDITOR_CONFIGS = {
    'default': {
        #'skin': 'moono',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock']},
            {'name': 'styles', 'items': []},
            {'name': 'colors', 'items': []},
            {'name': 'tools', 'items': ['Maximize']},
            {'name': 'about', 'items': ['About']},
            #'/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                #'Source'
            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
         'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
         'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            #'uploadimage', # the upload image feature
            # your extra plugins here
            #'div',
            #'autolink',
            #'autoembed',
            #'embedsemantic',
            #'autogrow',
            # 'devtools',
            #'widget',
            #'lineutils',
            #'clipboard',
            #'dialog',
            #'dialogui',
            #'elementspath'
        ]),
        'entities': False,
        'basicEntities': False,
        'fillEmptyBlocks': False,
        'autoParagraph': False,
    }
}
