from django.contrib import admin
from src.apps.patient.models import Patient


class PatientAdmin(admin.ModelAdmin):
    pass

admin.site.register(Patient, PatientAdmin)