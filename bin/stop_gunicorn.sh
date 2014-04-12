#!/bin/bash
export DJANGO_SETTINGS_MODULE=medhack.settings

PORT=`python -c 'from django.conf import settings;print settings.HTTP_PORT'`

# Kill all gunicorn instances running on port $PORT
ps auxww | grep gunicorn | grep $PORT | awk '{print $2}' | xargs kill
