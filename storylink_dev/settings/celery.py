import environ

env = environ.Env()

env = environ.Env(
    # set casting, default value
    TEST_CI=(bool, False),
)

# reading .env file
if (not env('TEST_CI')):
    environ.Env.read_env()


CELERY_EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
# CELERY CONF
CELERY_BROKER_URL = env('CELERY_BROKER_URL')
