#!/bin/bash

# Effectue les migrations
python manage.py migrate --noinput

# Collecte les fichiers statiques
python manage.py collectstatic --noinput

# Lance Gunicorn
exec gunicorn --bind 0.0.0.0:8000 --workers 3 deploymentapp.wsgi:application
