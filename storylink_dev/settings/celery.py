CELERY_EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
#CELERY CONF
CELERY_BROKER_URL = 'amqp://rabbit-user:rabbit12345@localhost:5672/stvhost'