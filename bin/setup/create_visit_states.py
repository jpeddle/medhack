import csv
from datetime import datetime
import os
from pprint import pprint
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medhack.settings")

from src.apps.visit.models import VisitState
# DO NOT REMOVE THIS
from src.apps.office_admin.models import BillingAddress, Insurance
from django.conf import settings

VISIT_STATES = (
    'Scheduled',
    'Registered',
    'Waiting to be seen by MD',
    'Complete',
)

def create_visit_states(verbose=False):

    for visit_state in VISIT_STATES:

        VisitState.objects.create(**{
            'state': visit_state,
        })


if __name__ == '__main__':
    create_visit_states()
