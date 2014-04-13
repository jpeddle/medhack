from django.db import models


class Patient(models.Model):
    MALE = 'm'
    FEMALE = 'f'

    SEXES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    first_name = models.CharField(max_length=255, null=True, blank=True)

    last_name = models.CharField(max_length=255, null=True, blank=True)

    billing_address = models.ForeignKey(to='office_admin.BillingAddress', related_name="patient_billing", null=True, blank=True)

    insurance = models.ForeignKey(to='office_admin.Insurance', related_name="patient_insurance", null=True, blank=True)

    phone = models.CharField(max_length=25, null=True, blank=True)

    dob = models.DateField(null=True, blank=True)

    mobile = models.CharField(max_length=25, null=True, blank=True)

    sex = models.CharField(max_length=1, choices=SEXES, null=True, blank=True)

    def __unicode__(self):
        return "%s: %s %s" % (self.pk, self.first_name, self.last_name)

    class Meta:
        db_table = 'patients'
        app_label = 'patient'

