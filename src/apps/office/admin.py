from django.contrib import admin
from src.apps.office.models import Doctor, Office

class DoctorAdmin(admin.ModelAdmin):
    pass

class OfficeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Office, OfficeAdmin)
