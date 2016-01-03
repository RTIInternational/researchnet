#!/bin/bash
echo Doing Routine Maintenance
python manage.py migrate                  # Apply database migrations
python manage.py collectstatic --noinput  # Collect static files
python manage.py bower install			  # install frontend assets

# Start Gunicorn processes
echo Starting Gunicorn
exec gunicorn config.wsgi:application -c /code/deployment/gunicorn.conf.py
