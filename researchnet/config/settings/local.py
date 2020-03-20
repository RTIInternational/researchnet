from .base import *

DEBUG = True

INTERNAL_IPS = ('127.0.0.1',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'researchnet',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

MIDDLEWARE += (
	'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS += (
	'debug_toolbar',
)

DEBUG_TOOLBAR_PANELS = [
	'debug_toolbar.panels.versions.VersionsPanel',
	'debug_toolbar.panels.timer.TimerPanel',
	'debug_toolbar.panels.settings.SettingsPanel',
	'debug_toolbar.panels.headers.HeadersPanel',
	'debug_toolbar.panels.request.RequestPanel',
	'debug_toolbar.panels.sql.SQLPanel',
	'debug_toolbar.panels.staticfiles.StaticFilesPanel',
	'debug_toolbar.panels.templates.TemplatesPanel',
	'debug_toolbar.panels.cache.CachePanel',
	'debug_toolbar.panels.signals.SignalsPanel',
	'debug_toolbar.panels.logging.LoggingPanel',
	'debug_toolbar.panels.redirects.RedirectsPanel',
]

# there will be problems later if these aren't set
assert 'EMAIL_HOST' in os.environ, 'Set EMAIL_HOST in your settings!'
assert 'EMAIL_HOST_USER' in os.environ, 'Set EMAIL_HOST_USER in your settings!'
assert 'EMAIL_HOST_PASSWORD' in os.environ, 'Set EMAIL_HOST_PASSWORD in your settings!'
assert 'EMAIL_PORT' in os.environ, 'Set EMAIL_PORT in your settings!'
assert 'EMAIL_USE_TLS' in os.environ, 'Set EMAIL_USE_TLS in your settings!'