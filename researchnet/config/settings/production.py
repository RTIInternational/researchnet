from .base import *


DEBUG = False
ALLOWED_HOSTS = ['*']

ADMINS = [('Adam', 'apreston@rti.org')]

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

