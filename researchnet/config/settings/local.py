from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'researchnet',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

# there will be problems later if these aren't set
assert 'EMAIL_HOST' in os.environ, 'Set EMAIL_HOST in your settings!'
assert 'EMAIL_HOST_USER' in os.environ, 'Set EMAIL_HOST_USER in your settings!'
assert 'EMAIL_HOST_PASSWORD' in os.environ, 'Set EMAIL_HOST_PASSWORD in your settings!'
assert 'EMAIL_PORT' in os.environ, 'Set EMAIL_PORT in your settings!'
assert 'EMAIL_USE_TLS' in os.environ, 'Set EMAIL_USE_TLS in your settings!'