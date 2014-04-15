from datetime import datetime
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from src.apps.schedule.models import Appointment

TZ = settings.PYTZ_TIMEZONE

DEMO_DATETIME = TZ.localize(datetime(2014, 4, 13))

@login_required
def upcoming_appointments(request):
    user = request.user

    patients = user.patients

    print str(DEMO_DATETIME)
    upcoming = Appointment.objects.filter(start_time__gte=DEMO_DATETIME, patient__user=user, visit__visit_state=1)

    current = Appointment.objects.filter(start_time__gte=DEMO_DATETIME, patient__user=user, visit__visit_state__in=(2,3))

    queue = {}

    for cur in current:
        visit_last_updated = TZ.normalize(cur.visit.last_updated)
        print str(visit_last_updated)
        print "visit_state: %s" % cur.visit.visit_state


        if cur.visit.visit_state.pk == 2:
            #check waiting room and exam room
            waiting_room_queue = Appointment.objects.filter(calendar__doctor=cur.calendar.doctor, visit__visit_state=2, visit__last_updated__lt=visit_last_updated).count()
            exam_room_queue = Appointment.objects.filter(calendar__doctor=cur.calendar.doctor, visit__visit_state=3).count()

            cur.waiting_room_queue = waiting_room_queue
            cur.exam_room_queue = exam_room_queue

            print "num in waiting room: %s" % cur.waiting_room_queue
            print "num in exam room: %s" % cur.exam_room_queue

        elif cur.visit.visit_state.pk == 3:
            # only check exam rooms
            cur.exam_room_queue = Appointment.objects.filter(calendar__doctor=cur.calendar.doctor, visit__visit_state=3, visit__last_updated__lt=visit_last_updated).count()

            print "num in exam room: %s" % cur.exam_room_queue

    return render(
        request,
        template_name='patient/upcoming_appointments.html',
        dictionary={
            'patients': patients,
            'upcoming': upcoming,
            'current': current,
            'page_name': 'upcoming'
        }
    )




@login_required
def family_members(request):
    user = request.user

    patients = user.patients

    return render(
        request,
        template_name='patient/family.html',
        dictionary={
            'patients': patients,
            'page_name': 'family'
        }
    )


@login_required
def billing_information(request):
    user = request.user

    patients = user.patients

    return render(
        request,
        template_name='patient/billing.html',
        dictionary={
            'patients': patients,
            'page_name': 'billing'
        }
    )


@login_required
def insurance_information(request):
    user = request.user

    patients = user.patients

    return render(
        request,
        template_name='patient/insurance.html',
        dictionary={
            'patients': patients,
            'page_name': 'insurance'
        }
    )

