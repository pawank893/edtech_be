#!/bin/bash

python manage.py collectstatic --noinput

DJANGO_DIR=/var/www/edtech/be/code/edtech
DJANGO_WSGI_MODULE=wsgi

DJANGO_SETTINGS_MODULE=edtech.settings.prod
DJANGO_CONFIGURATION=Prod

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export DJANGO_CONFIGURATION=$DJANGO_CONFIGURATION

python manage.py migrate --noinput

gunicorn -c $DJANGO_DIR/guniconfig.py $DJANGO_WSGI_MODULE
