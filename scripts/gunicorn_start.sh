#!/bin/bash

python manage.py collectstatic --noinput

DJANGO_DIR=/var/www/edtech/be/code/edtech
DJANGO_WSGI_MODULE=wsgi

python manage.py migrate --noinput

exec gunicorn -c $DJANGO_DIR/config/guniconfig.py $DJANGO_WSGI_MODULE
