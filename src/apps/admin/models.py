from django.db import models


class Insurance(models.Model):

    provider = models.CharField(max_length=255, null=False, blank=False)

    group_id = models.CharField(max_length=255, null=False, blank=False)

    plan_id = models.CharField(max_length=255, null=False, blank=False)


class BillingAddress(models.Model):

    address1 = models.CharField(max_length=255, null=True, blank=True)

    address2 = models.CharField(max_length=255, null=True, blank=True)

    city = models.CharField(max_length=255, null=True, blank=True)

    state = models.CharField(max_length=255, null=True, blank=True)

    zip = models.CharField(max_length=255, null=True, blank=True)

