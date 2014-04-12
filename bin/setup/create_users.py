import csv
from datetime import datetime
import os
from pprint import pprint
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medhack.settings")

from django.contrib.auth.models import User
from django.conf import settings
# from src.apps.users import models

USER_CSV = 'users.csv'

#pipe char
DELIMITER = '|'
QUOTE_CHAR = '"'

def read_csv(csv_file):
    records = []

    with open(csv_file, 'r+') as r:
        names = r.readline()
        names = names.strip().replace(QUOTE_CHAR, '').split(DELIMITER)

        csvreader = csv.DictReader(r, fieldnames=names, delimiter=DELIMITER, quotechar=QUOTE_CHAR)
        for row in csvreader:
            row = dict((k.lower(), v.decode("windows-1252")) for k, v in row.iteritems())

            records.append(row)

    return records


def user_dict_to_obj(data_dict):
    # pprint(data_dict)
    user = User(
        username=data_dict['username'],
        first_name=data_dict['first_name'],
        last_name=data_dict['last_name'],
    )

    user.is_staff = True
    user.is_superuser = True
    user.set_password(data_dict['password'])

    user.save()


def create_users(verbose=False):
    csv_file = os.path.join(settings.CSV_DIR, USER_CSV)

    print "parsing file: %s" % csv_file

    users = read_csv(csv_file)

    if verbose:
        pprint(users)

    for user in users:
        user_dict_to_obj(user)


if __name__ == '__main__':
    create_users()
