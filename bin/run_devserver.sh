#!/bin/bash

# devserver is broken for django 1.6+
# python manage.py runserver --werkzeug

python manage.py runserver_plus 8000
