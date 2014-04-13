from crispy_forms.bootstrap import FormActions, StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field
from django import forms
from django.db import models


class Calendar(models.Model):

    name = models.CharField(max_length=255, null=False, blank=False)

    doctor = models.ForeignKey(to='office.Doctor', related_name='calendar')

    class Meta:
        db_table = 'calendars'
        app_label = 'schedule'


class Appointment(models.Model):

    calendar = models.ForeignKey(to=Calendar, related_name='appointment')

    patient = models.ForeignKey(to='patient.Patient', related_name='appointments')

    visit = models.ForeignKey(to='visit.Visit')

    start_time = models.DateTimeField()

    end_time = models.DateTimeField()

    pre_checkin_completed = models.BooleanField(default=False)

    call_for_reschedule = models.BooleanField(default=False)

    call_for_reschedule_time = models.DateTimeField(null=True, blank=True)

    change_in_symptoms = models.TextField(null=True, blank=True, verbose_name="Change in Symptoms?")

    patient_questions = models.TextField(null=True, blank=True, verbose_name="Questions for the Doctor? ")

    class Meta:
        db_table = 'appointments'
        app_label = 'schedule'


class AppointmentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.render_unmentioned_fields = False
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'

        self.helper.layout = Layout(
            Fieldset(
                'Other Information',
                Field('change_in_symptoms'),
                Field('patient_questions'),
            ),
            FormActions(
                StrictButton('Submit', type='submit', css_class='btn btn-primary pull-right')
            )
        )

    class Meta:
        model = Appointment
        exclude = ['calendar', 'patient', 'visit', 'start_time', 'end_time', 'pre_checkin_completed', 'call_for_reschedule', 'call_for_reschedule_time']



