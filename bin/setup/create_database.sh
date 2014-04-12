#!/bin/sh

export DJANGO_SETTINGS_MODULE=medhack.settings
DB_USER=`python -c 'from django.conf import settings;print settings.DB_USER'`
DB_PASSWORD=`python -c 'from django.conf import settings;print settings.DB_PASSWORD'`
DB_NAME=`python -c 'from django.conf import settings;print settings.DB_NAME'`

echo "DROP user '$DB_USER' - MySQL Root PW"
echo "DROP USER '$DB_USER'@'localhost'" | mysql -u root -p

echo "CREATE user '$DB_USER' - MySQL Root PW"
echo "CREATE USER '$DB_USER'@'localhost' IDENTIFIED BY '$DB_PASSWORD'; GRANT ALL PRIVILEGES ON *.* TO '$DB_USER'@'localhost' WITH GRANT OPTION;" | mysql -u root -p

echo "DROP database '$DB_NAME'"
echo "DROP DATABASE $DB_NAME;" | mysql -u $DB_USER -p$DB_PASSWORD

echo "CREATE database '$DB_NAME'"
echo "CREATE DATABASE $DB_NAME;" | mysql -u $DB_USER -p$DB_PASSWORD

