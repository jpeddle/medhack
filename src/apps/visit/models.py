from datetime import datetime
from django.db import models
import pytz

EASTERN_TIMEZONE = pytz.timezone('US/Eastern')

class VisitState(models.Model):
    
    state = models.CharField(max_length=255, null=False, blank=False)
    
    class Meta:
        db_table = 'visit_states'
        app_label = 'visit'


class VisitStateHistory(models.Model):

    visit_state = models.ForeignKey(to=VisitState)

    time_created = models.DateTimeField()

    time_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'visit_state_history'
        app_label = 'visit'


class VisitManager(models.Manager):

    def create_visit(self):
        visit_history = VisitStateHistory.objects.create(**{
            'visit_state': VisitState.objects.get(pk=1),
            'time_created': EASTERN_TIMEZONE.localize(datetime.now()),
        })

        visit = Visit.objects.create(**{
            'visit_state': VisitState.objects.get(pk=1),
            'visit_state_history': visit_history
        })

        return visit


    def update_visit(self):
        pass


class Visit(models.Model):

    visit_state = models.ForeignKey(to=VisitState)

    visit_state_history = models.ForeignKey(to=VisitStateHistory)

    last_updated = models.DateTimeField(null=False, blank=False, auto_now=True)

    objects = VisitManager()

    class Meta:
        db_table = 'visits'
        app_label = 'visit'

