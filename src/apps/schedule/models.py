from django.db import models


class Calendar(models.Model):

    name = models.CharField(max_length=255, null=False, blank=False)

    doctor = models.ForeignKey(to='office.Doctor')


class Appointment(models.Model):

    calendar = models.ForeignKey(to=Calendar)

    patient = models.ForeignKey(to='patient.Patient')

    visit = models.ForeignKey(to='visit.Visit')

    appointment_start_time = models.DateTimeField()

    appointment_end_time = models.DateTimeField()

