from django.db import models


class Office(models.Model):

    name = models.CharField(max_length=255, null=True, blank=True)

    address1 = models.CharField(max_length=255, null=True, blank=True)

    address2 = models.CharField(max_length=255, null=True, blank=True)

    city = models.CharField(max_length=255, null=True, blank=True)

    state = models.CharField(max_length=255, null=True, blank=True)

    zip = models.CharField(max_length=255, null=True, blank=True)

    number_exam_rooms = models.IntegerField()

    class Meta:
        db_table = 'offices'
        app_label = 'office'


class Doctor(models.Model):

    first_name = models.CharField(max_length=255, null=True, blank=True)

    last_name = models.CharField(max_length=255, null=True, blank=True)

    office = models.ForeignKey(to=Office, related_name='doctors', null=False, blank=False)

    about = models.TextField()

    class Meta:
        db_table = 'doctors'
        app_label = 'office'
