from .base import *

# Obviously this shouldn't be true but until the web proxy is setup (and nginx serves up the static files) we have to run the app in debug mode.

DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
