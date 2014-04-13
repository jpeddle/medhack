import csv
from datetime import datetime
import os
from pprint import pprint
import sys
import pytz

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medhack.settings")

from src.apps.visit.models import Visit, VisitState
from src.apps.office.models import Doctor, Office
from src.apps.patient.models import Patient
from src.apps.schedule.models import Calendar, Appointment
# DO NOT REMOVE THIS
from src.apps.office_admin.models import BillingAddress, Insurance
from django.conf import settings

USER_CSV = 'appointments.csv'

TZ = settings.PYTZ_TIMEZONE

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


def appointment_dict_to_obj(data_dict):
    # pprint(data_dict)

    patient = Patient.objects.get(pk=data_dict['patient_id'])
    doctor = Doctor.objects.get(pk=data_dict['doctor_id'])

    visit = Visit.objects.create_visit()

    appointment = Appointment(
        patient=patient,
        calendar=doctor.calendar.get(),
        visit=visit,
        start_time=TZ.localize(datetime.strptime(data_dict['start_time'], '%m/%d/%y %I:%M %p')),
        end_time=TZ.localize(datetime.strptime(data_dict['end_time'], '%m/%d/%y %I:%M %p')),
    )

    appointment.save()


def create_appointments(verbose=False):
    csv_file = os.path.join(settings.CSV_DIR, USER_CSV)

    print "parsing file: %s" % csv_file

    appointments = read_csv(csv_file)

    if verbose:
        pprint(appointments)

    for appointment in appointments:
        appointment_dict_to_obj(appointment)


if __name__ == '__main__':
    create_appointments()
