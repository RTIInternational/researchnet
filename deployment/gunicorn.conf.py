import multiprocessing

raw_env=["DJANGO_SETTINGS_MODULE=config.settings.production"]
bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
timeout = 30
loglevel = "debug"
secure_scheme_headers = { 'X-FORWARDED-PROTO': 'https'}
