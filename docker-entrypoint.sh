#!/bin/bash

APP_NAME=fampay_test
DIR=/app/
LOG_LEVEL=
MAX_NO_REQUESTS_PER_WORKER=
JITTER=

#Sleep until db comesup
sleep 45
#RUN Migrations
python3 manage.py makemigrations youtube
python3 manage.py migrate youtube

#Start server as gunicorn
gunicorn fampay_test.wsgi:application \
      --bind 0.0.0.0:8000 \
      --max-requests 1000 \
      --max-requests-jitter 50 \
      --workers 3 \
      --access-logfile='-' \
      --access-logformat='%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(p)s" "%(D)s"'
