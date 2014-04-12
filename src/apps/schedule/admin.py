from django.contrib import admin
from src.apps.schedule.models import Appointment, Calendar


class AppointmentAdmin(admin.ModelAdmin):
    pass

class CalendarAdmin(admin.ModelAdmin):
    pass

admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Calendar, CalendarAdmin)
