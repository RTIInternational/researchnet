#!/bin/bash
echo Doing Routine Maintenance
python manage.py migrate                  # Apply database migrations
python manage.py collectstatic --noinput  # Collect static files
python manage.py bower install			  # install frontend assets

# Start Gunicorn processes
echo Starting Gunicorn
exec gunicorn config.wsgi:application \
    --name researchnet \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --timeout 30 \
	--log-level=debug \
    "$@"