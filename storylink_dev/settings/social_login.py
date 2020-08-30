import environ

env = environ.Env()

env = environ.Env(
    # set casting, default value
    TEST_CI=(bool, False),
)

# reading .env file
if (not env('TEST_CI')):
    environ.Env.read_env()


# para inicio sesion facebook
AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    # 'django.contrib.auth.backends.ModelBackend',
    'django.contrib.auth.backends.AllowAllUsersModelBackend',
)


SOCIAL_AUTH_FACEBOOK_KEY = env('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = env('SOCIAL_AUTH_FACEBOOK_SECRET')

SOCIAL_AUTH_USER_MODEL = 'users.CustomUser'

# para forzar a pedir el email
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
LOGIN_ERROR_URL = '/'

SOCIAL_AUTH_RAISE_EXCEPTIONS = False


SOCIAL_AUTH_POSTGRES_JSONFIELD = True

# por las dudas no entendi por que, pero es bueno setear la siguiente variable
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'email']

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'apps.users.pipeline.require_email',
    # 'apps.users.pipeline.get_username', #custom get_username
    # 'apps.users.pipeline.check_unique_username', # check username
    'social_core.pipeline.user.get_username',
    # 'apps.users.pipeline.username_check',
    # 'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    # 'apps.users.pipeline.get_avatar_url',
    'apps.users.pipeline.update_or_create_userProfile',
)


SESSION_COOKIE_SAMESITE = None

SOCIAL_AUTH_FIELDS_STORED_IN_SESSION = ['email', ]
SOCIAL_AUTH_FIELDS_STORED_IN_SESSION = ['username', ]


SOCIAL_AUTH_FACEBOOK_API_VERSION = '6.0'
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# inicio de sesion con twitter

SOCIAL_AUTH_TWITTER_KEY = env('SOCIAL_AUTH_TWITTER_KEY')
SOCIAL_AUTH_TWITTER_SECRET = env('SOCIAL_AUTH_TWITTER_SECRET')

SOCIAL_AUTH_TWITTER_EXTRA_DATA = [                 # add this
    ('name', 'name'),
    ('email', 'email'),
    ('profile_image_url', 'link_img_perfil'),
]
