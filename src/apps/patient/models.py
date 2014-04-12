from django.db import models


class Patient(models.Model):

    first_name = models.CharField(max_length=255, null=True, blank=True)

    last_name = models.CharField(max_length=255, null=True, blank=True)

    billing_address = models.ForeignKey(to='admin.BillingAddress', null=True, blank=True)

    insurance = models.ForeignKey(to='admin.Insurance', null=True, blank=True)

    phone = models.CharField(max_length=25, null=True, blank=True)

    dob = models.DateField(null=True, blank=True)

    mobile = models.CharField(max_length=25, null=True, blank=True)

    sex = models.CharField(max_length=1, null=True, blank=True)


