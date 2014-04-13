from django.contrib import admin
from src.apps.visit.models import Visit, VisitState, VisitStateHistory


class VisitAdmin(admin.ModelAdmin):
    pass

class VisitStateAdmin(admin.ModelAdmin):
    pass

class VisitStateHistoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Visit, VisitAdmin)
admin.site.register(VisitState, VisitStateAdmin)
admin.site.register(VisitStateHistory, VisitStateHistoryAdmin)

