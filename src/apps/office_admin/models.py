from crispy_forms.bootstrap import FormActions, StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field
from django import forms
from django.db import models


class Insurance(models.Model):

    provider = models.CharField(max_length=255, null=False, blank=False)

    group_id = models.CharField(max_length=255, null=False, blank=False)

    plan_id = models.CharField(max_length=255, null=False, blank=False)

    patient = models.ForeignKey(to='patient.Patient', related_name='insurance', blank=True, null=True)

    offices = models.ManyToManyField('office.Office', related_name='patient_insurance', blank=True, null=True)


    class Meta:
        db_table = 'insurance'
        app_label = 'office_admin'


class InsuranceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InsuranceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.render_unmentioned_fields = False
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'

        self.helper.layout = Layout(
            Fieldset(
                'Insurance',
                Field('provider'),
                Field('group_id'),
                Field('plan_id'),
            ),
            FormActions(
                StrictButton('Next', type='submit', css_class='btn btn-primary pull-right')
            )
        )

    class Meta:
        model = Insurance
        exclude = ['patient', 'offices']


class BillingAddress(models.Model):

    address1 = models.CharField(max_length=255, null=True, blank=True)

    address2 = models.CharField(max_length=255, null=True, blank=True)

    city = models.CharField(max_length=255, null=True, blank=True)

    state = models.CharField(max_length=255, null=True, blank=True)

    zip = models.CharField(max_length=255, null=True, blank=True)

    patient = models.ForeignKey(to='patient.Patient', related_name='billing_addresses', blank=True, null=True)

    offices = models.ManyToManyField(to='office.Office', related_name='patient_billing_addresses', blank=True, null=True)

    class Meta:
        db_table = 'billing_addresses'
        app_label = 'office_admin'


class BillingAddressForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BillingAddressForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.render_unmentioned_fields = False
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'

        self.helper.layout = Layout(
            Fieldset(
                'Billing Address',
                Field('address1'),
                Field('address2'),
                Field('city'),
                Field('state'),
                Field('zip'),
            ),
            FormActions(
                StrictButton('Next', type='submit', css_class='btn btn-primary pull-right')
            )
        )

    class Meta:
        model = BillingAddress
        exclude = ['patient', 'offices']
