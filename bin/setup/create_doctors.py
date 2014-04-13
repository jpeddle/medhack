import csv
from datetime import datetime
import os
from pprint import pprint
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medhack.settings")

from src.apps.office.models import Doctor, Office
# DO NOT REMOVE THIS
from src.apps.office_admin.models import BillingAddress, Insurance
from django.conf import settings

USER_CSV = 'doctors.csv'

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
            row = dict((k.lower(), v) for k, v in row.iteritems())

            records.append(row)

    return records


def doctor_dict_to_obj(data_dict, office):
    # pprint(data_dict)
    doctor = Doctor(
        first_name=data_dict['first_name'],
        last_name=data_dict['last_name'],
        office=office
    )

    doctor.save()


def create_doctors(verbose=False):
    csv_file = os.path.join(settings.CSV_DIR, USER_CSV)

    print "parsing file: %s" % csv_file

    doctors = read_csv(csv_file)

    office = Office.objects.get(pk=1)

    if verbose:
        pprint(doctors)

    for doctor in doctors:
        doctor_dict_to_obj(doctor, office)


if __name__ == '__main__':
    create_doctors()
