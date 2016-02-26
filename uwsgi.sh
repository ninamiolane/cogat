#!/bin/bash
while ! nc -z graphdb 7474; do sleep 3; done

python /code/manage.py makemigrations
python /code/manage.py migrate
python /code/manage.py collectstatic --noinput
uwsgi --ini /code/uwsgi.ini
