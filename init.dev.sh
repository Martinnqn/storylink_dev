#!/bin/sh
echo "initv"
pwd
./manage.py collectstatic --noinput
./manage.py makemigrations
./manage.py migrate
gunicorn --bind 0.0.0.0:8000 storylink_dev.wsgi --reload