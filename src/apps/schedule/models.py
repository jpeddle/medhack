from django.db import models


class Calendar(models.Model):

    name = models.CharField(max_length=255, null=False, blank=False)

    doctor = models.ForeignKey(to='office.Doctor', related_name='calendar')

    class Meta:
        db_table = 'calendars'
        app_label = 'schedule'


class Appointment(models.Model):

    calendar = models.ForeignKey(to=Calendar, related_name='appointment')

    patient = models.ForeignKey(to='patient.Patient')

    visit = models.ForeignKey(to='visit.Visit')

    start_time = models.DateTimeField()

    end_time = models.DateTimeField()

    class Meta:
        db_table = 'appointments'
        app_label = 'schedule'
