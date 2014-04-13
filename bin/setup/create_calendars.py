import csv
from datetime import datetime
import os
from pprint import pprint
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medhack.settings")

from src.apps.office.models import Doctor
from src.apps.schedule.models import Calendar
# DO NOT REMOVE THIS
from src.apps.office_admin.models import BillingAddress, Insurance
from django.conf import settings

def create_calendars(verbose=False):

    doctors = Doctor.objects.all()

    for doctor in doctors:
        calendar_name = "%s %s's Calendar" % (doctor.first_name, doctor.last_name)

        Calendar.objects.create(**{
            'name': calendar_name,
            'doctor': doctor
        })


if __name__ == '__main__':
    create_calendars()
