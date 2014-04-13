from datetime import datetime
from django.shortcuts import render
from src.apps.schedule.models import Appointment
from src.apps.visit.models import VisitState


def get_by_date(request, year, month, day):

    appointments = Appointment.objects.filter(
        start_time__year=int(year),
        start_time__month=int(month),
        start_time__day=int(day)).order_by('patient__last_name')

    visit_states = VisitState.objects.all().order_by('id')


    return render(
        request,
        template_name='schedule/view_by_date.html',
        dictionary={
            'appointments': appointments,
            'visit_states': visit_states,
        }
    )