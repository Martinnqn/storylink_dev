#configuracion correo
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_HOST_USER = 'storylink@hotmail.com'
DEFAULT_FROM_EMAIL = 'storylink@hotmail.com'
EMAIL_HOST_PASSWORD = '38082317story'
EMAIL_PORT = 587