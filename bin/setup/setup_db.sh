#!/bin/bash

export DJANGO_SETTINGS_MODULE=medhack.settings
MODE=`python -c 'from django.conf import settings;print settings.MODE'`

echo "Using mode: '$MODE'"

if [ "$MODE" == "dev" ]; then
    echo "Dropping SQLITE3 DB"
    rm db.sqlite3

elif [ $MODE == "test" ] || [ $MODE == "prod" ]; then
    echo "Running create DB script"
    bin/setup/create_database.sh
fi


#python -u bin/setup/create_index.py
echo "no" | python manage.py syncdb
python -u bin/setup/create_users.py
#python -u bin/setup/create_classifications.py
