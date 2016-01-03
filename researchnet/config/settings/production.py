from .base import *

# Obviously this shouldn't be true but until the web proxy is setup (and nginx serves up the static files) we have to run the app in debug mode.
DEBUG = True
ALLOWED_HOSTS = ['*']

