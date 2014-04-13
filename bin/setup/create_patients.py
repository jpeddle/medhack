import csv
from datetime import datetime
import os
from pprint import pprint
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medhack.settings")

from django.contrib.auth.models import User
from src.apps.patient.models import Patient
# DO NOT REMOVE THIS
from src.apps.office_admin.models import BillingAddress, Insurance
from django.conf import settings

USER_CSV = 'patients.csv'

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


def patient_dict_to_obj(data_dict):
    # pprint(data_dict)
    patient = Patient(
        first_name=data_dict['first_name'],
        last_name=data_dict['last_name'],
        dob=datetime.strptime(data_dict['dob'], '%m/%d/%y'),
        sex=data_dict['sex'].lower(),
        phone=data_dict['phone'],
        mobile=data_dict['phone'],
    )

    patient.save()

    if User.objects.filter(first_name=patient.first_name).exists():
        patient.user = User.objects.get(first_name=patient.first_name)
        patient.save()



def create_patients(verbose=False):
    csv_file = os.path.join(settings.CSV_DIR, USER_CSV)

    print "parsing file: %s" % csv_file

    patients = read_csv(csv_file)

    if verbose:
        pprint(patients)

    for patient in patients:
        patient_dict_to_obj(patient)


if __name__ == '__main__':
    create_patients()
