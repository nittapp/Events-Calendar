#!/bin/bash
echo "STARTING APP...."

# Initialize Django project
python /usr/src/app/manage.py collectstatic --noinput
python /usr/src/app/manage.py makemigrations
python /usr/src/app/manage.py migrate --noinput