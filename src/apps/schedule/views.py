from datetime import datetime, timedelta
import logging
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from src.apps.office_admin.models import BillingAddressForm, InsuranceForm
from src.apps.schedule.models import Appointment, Calendar, AppointmentForm
from src.apps.visit.models import VisitState
from src.lib.twilio_client import TwilioClient
import simplejson as json

logger = logging.getLogger(settings.MEDHACK_LOG)

TZ = settings.PYTZ_TIMEZONE

DEMO_DATETIME = TZ.localize(datetime(2014, 4, 13))

DEMO_ALERT = TZ.localize(datetime(2014, 4, 13, 13, 30))

def get_appointments_by_date(year, month, day):
    appointments = Appointment.objects.filter(
        start_time__year=int(year),
        start_time__month=int(month),
        start_time__day=int(day))

    return appointments


def get_by_date(request, calendar_id, year, month, day):

    date = datetime(int(year), int(month), int(day))

    appointments = get_appointments_by_date(year, month, day).order_by('patient__last_name')
    calendar = Calendar.objects.get(pk=calendar_id)

    visit_states = VisitState.objects.all().order_by('id')

    return render(
        request,
        template_name='schedule/view_by_date.html',
        dictionary={
            'date': date,
            'appointments': appointments,
            'visit_states': visit_states,
            'calendar': calendar,
            'page_name': 'appointments'
        }
    )


twilio = TwilioClient()

def notify_daily(request):

    appointments = get_appointments_by_date(DEMO_DATETIME.year, DEMO_DATETIME.month, DEMO_DATETIME.day).order_by("start_time")
    twilio.alert_daily([appointments.first()])

    return HttpResponse("Successfully notified %s appointments" % appointments.count())


def notify_status(request):

    appointment_time = DEMO_ALERT + timedelta(hours=1)
    logger.info("Query for %s" % appointment_time)

    appointments = Appointment.objects.filter(
        start_time__year=appointment_time.year,
        start_time__month=appointment_time.month,
        start_time__day=appointment_time.day,
        start_time__hour=appointment_time.hour,
        start_time__minute=appointment_time.minute)

    latest_appointment = get_appointments_by_date(DEMO_DATETIME.year, DEMO_DATETIME.month, DEMO_DATETIME.day).order_by("start_time").exclude(visit__visit_state_id=4).first()

    latest_time = TZ.normalize(latest_appointment.start_time)
    logger.info("Latest appointment: %s" % latest_time)

    minutes_behind = int((DEMO_ALERT - latest_time).total_seconds()/60)
    logger.info("Minutes behind: %s" % minutes_behind)

    for appointment in appointments:
        start_time = TZ.normalize(appointment.start_time).strftime("%I:%M %p")
        logger.info("%s: %s %s" % (appointment.id, start_time, appointment.visit.visit_state.state))

        twilio.alert_status(appointment, minutes_behind)

        appointment.call_for_reschedule = True
        appointment.call_for_reschedule_time = DEMO_ALERT + timedelta(minutes=30)
        appointment.save()

    return HttpResponse("Successfully notified %s appointments" % appointments.count())


def mark_rescheduled(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)

    appointment.call_for_reschedule = False
    appointment.call_for_reschedule_time = None
    appointment.save()

    return HttpResponse(json.dumps({'success': True}), content_type="application/json")


def checkin_billing(request, appointment_id):

    appointment = Appointment.objects.get(pk=appointment_id)

    if request.method == "GET":

        form = BillingAddressForm()

        return render(
            request,
            template_name='schedule/checkin_billing.html',
            dictionary={
                'appointment': appointment,
                'form': form,
            }
        )

    elif request.method == "POST":
        form = BillingAddressForm(request.POST or None)

        if form.is_valid():
            logger.info("BillingAddress is valid")
            billing_address = form.save(commit=False)
            billing_address.patient = appointment.patient
            billing_address.save()
            billing_address.offices.add(appointment.calendar.doctor.office)

            return HttpResponseRedirect('/appointment/%s/checkin/insurance/' % appointment.id)


def call_for_reschedule(request):
    appointments = Appointment.objects.filter(call_for_reschedule=True)

    return render(
        request,
        template_name='schedule/call_for_reschedule.html',
        dictionary={
            'appointments': appointments,
            'page_name': 'calls'
        }
    )



def checkin_insurance(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)

    if request.method == "GET":

        form = InsuranceForm()

        return render(
            request,
            template_name='schedule/checkin_insurance.html',
            dictionary={
                'appointment': appointment,
                'form': form,
            }
        )

    elif request.method == "POST":
        form = InsuranceForm(request.POST or None)

        if form.is_valid():
            logger.info("Insurance is valid")
            insurance = form.save(commit=False)
            insurance.patient = appointment.patient
            insurance.save()
            insurance.offices.add(appointment.calendar.doctor.office)

            appointment.pre_checkin_completed = True
            appointment.save()

            return HttpResponseRedirect('/appointment/%s/checkin/other/' % appointment.id)


def checkin_other(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)

    if request.method == "GET":

        form = AppointmentForm()

        return render(
            request,
            template_name='schedule/checkin_other.html',
            dictionary={
                'appointment': appointment,
                'form': form,
            }
        )

    elif request.method == "POST":
        form = AppointmentForm(request.POST)

        if form.is_valid():
            logger.info("Appointment is valid")

            appointment.change_in_symptoms = form.cleaned_data['change_in_symptoms']
            appointment.patient_questions = form.cleaned_data['patient_questions']

            appointment.pre_checkin_completed = True
            appointment.save()

            return HttpResponseRedirect('/appointment/%s/checkin/complete/' % appointment.id)


def checkin_complete(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    office = appointment.calendar.doctor.office

    billing_address = appointment.patient.billing_addresses.get(offices=office)
    insurance = appointment.patient.insurance.get(offices=office)

    return render(
        request,
        template_name="schedule/checkin_complete.html",
        dictionary={
            'appointment': appointment,
            'insurance': insurance,
            'billing_address': billing_address,
        }
    )

