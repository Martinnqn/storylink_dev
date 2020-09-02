import os
import environ

env = environ.Env()

# reading .env file
if (not os.environ.get('CI')):
    environ.Env.read_env()


CELERY_EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
# CELERY CONF
CELERY_BROKER_URL = env('CELERY_BROKER_URL')
