#!/bin/bash

export DJANGO_SETTINGS_MODULE=medhack.settings

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

HOST=localhost
PORT=`python -c 'from django.conf import settings;print settings.HTTP_PORT'`
WORKERS=2
TIMEOUT=120
echo "Starting Gunicorn at $HOST:$PORT"

~/.virtualenvs/medhack/bin/gunicorn -b $HOST:$PORT -w=$WORKERS -t $TIMEOUT --log-file gunicorn.log medhack.wsgi:application

