"""
Django settings for storylink_dev project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6-v$$swa_e8*9i4ga#37#w&c$tr5_&#cjy!d^ymf*i@s2wsct+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '192.168.1.39', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.users',
    'apps.publications',
    'widget_tweaks',
    'django_bleach',
    'ckeditor',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'storylink_dev.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'static/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'storylink_dev.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nk_db',
        'USER': 'nk_user',
        'HOST': 'localhost',
        'PASSWORD': '1234',
        'client_encoding': 'UTF8',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
]
'''
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
'''

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    'static/',
]
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


AUTH_USER_MODEL = 'users.CustomUser'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

#configuracion django-bleach

# Which HTML tags are allowed
BLEACH_ALLOWED_TAGS = ['p', 'b', 'i', 'u', 'ul', 'li' 'ol', 'em', 'strong', 'span', 's']

# Which HTML attributes are allowed
BLEACH_ALLOWED_ATTRIBUTES = ['style']

# Which CSS properties are allowed in 'style' attributes (assuming style is
# an allowed attribute)
BLEACH_ALLOWED_STYLES = ['text-decoration', 'color', 'background-color', 'text-align']

# Which protocols (and pseudo-protocols) are allowed in 'src' attributes
# (assuming src is an allowed attribute)
BLEACH_ALLOWED_PROTOCOLS = []

# Strip unknown tags if True, replace with HTML escaped characters if False
BLEACH_STRIP_TAGS = False

# Strip HTML comments, or leave them in.
BLEACH_STRIP_COMMENTS = False

BLEACH_DEFAULT_WIDGET = 'ckeditor.widgets.CKEditorWidget'

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
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
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
    }
}

#para inicio sesion facebook
AUTHENTICATION_BACKENDS=(
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    )


SOCIAL_AUTH_FACEBOOK_KEY = '1606554956167156'
SOCIAL_AUTH_FACEBOOK_SECRET = '93ef55779217814620b94a889c9a5ad1'

SOCIAL_AUTH_USER_MODEL = 'users.CustomUser'

#para forzar a pedir el email
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {       # add this
  'fields': 'id, name, email, picture.type(large)'
}
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [                 # add this
    ('name', 'name'),
    ('email', 'email'),
    ('picture', 'link_img_perfil'),
]

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/'
SOCIAL_AUTH_LOGIN_URL = '/'
SOCIAL_AUTH_BACKEND_ERROR_URL = '/'
LOGIN_ERROR_URL= '/'

SOCIAL_AUTH_RAISE_EXCEPTIONS = False


SOCIAL_AUTH_POSTGRES_JSONFIELD = True

#por las dudas no entendi por que, pero es bueno setear la siguiente variable
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'email']

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'apps.users.pipeline.require_email',
    #'apps.users.pipeline.get_username', #custom get_username
    #'apps.users.pipeline.check_unique_username', # check username
    'social_core.pipeline.user.get_username',
    #'apps.users.pipeline.username_check',
    #'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)


SESSION_COOKIE_SAMESITE = None

SOCIAL_AUTH_FIELDS_STORED_IN_SESSION = ['email',]
SOCIAL_AUTH_FIELDS_STORED_IN_SESSION = ['username',]

