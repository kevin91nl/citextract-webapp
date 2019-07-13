#!/bin/sh
python manage.py migrate --noinput && echo "Migrations done!"
python manage.py runserver 0.0.0.0:8000