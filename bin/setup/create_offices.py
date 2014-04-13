import csv
from datetime import datetime
import os
from pprint import pprint
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medhack.settings")

from src.apps.office.models import Office
# DO NOT REMOVE THIS
from src.apps.office_admin.models import BillingAddress, Insurance
from django.conf import settings

USER_CSV = 'offices.csv'

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


def office_dict_to_obj(data_dict):
    # pprint(data_dict)
    office = Office(
        name=data_dict['name'],
        address1=data_dict['address1'],
        address2=data_dict['address2'],
        city=data_dict['city'],
        state=data_dict['state'],
        zip=data_dict['zip'],
        number_exam_rooms=data_dict['number_exam_rooms'],
    )

    office.save()


def create_offices(verbose=False):
    csv_file = os.path.join(settings.CSV_DIR, USER_CSV)

    print "parsing file: %s" % csv_file

    offices = read_csv(csv_file)

    if verbose:
        pprint(offices)

    for office in offices:
        office_dict_to_obj(office)


if __name__ == '__main__':
    create_offices()
