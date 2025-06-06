#!/bin/bash

echo "..................Starting cron service.................."
service cron start

echo "..................Removing Django cron jobs.................."
rm -f /server/.crontab
crontab -r || true
echo "..................Adding Django cron jobs.................."
python manage.py crontab add
# python manage.py crontab remove
# python manage.py crontab add

echo "..................Starting Django makemigrations.................."
python manage.py makemigrations

echo "..................Starting Django migrations.................."
python manage.py migrate

echo "..................Starting Django server.................."
python manage.py runserver 0.0.0.0:8000
