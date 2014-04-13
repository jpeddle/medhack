from datetime import datetime
from django.conf import settings
from django.db import models
import pytz

TZ = settings.PYTZ_TIMEZONE

class VisitState(models.Model):
    
    state = models.CharField(max_length=255, null=False, blank=False)
    
    class Meta:
        db_table = 'visit_states'
        app_label = 'visit'


class VisitManager(models.Manager):

    def create_visit(self):

        visit = Visit.objects.create(**{
            'visit_state': VisitState.objects.get(pk=1),
            # 'visit_state_history': visit_history
        })

        return visit


    def update_visit(self, visit_id, visit_state_id):
        print "updating visit: %s" % visit_id

        visit = Visit.objects.get(pk=visit_id)

        visit_history = VisitStateHistory.objects.create(**{
            'visit': visit,
            'visit_state': visit.visit_state,
            'time_created': visit.last_updated,
            'time_updated': TZ.localize(datetime.now())
        })

        visit_state = VisitState.objects.get(pk=visit_state_id)
        visit.visit_state = visit_state
        visit.last_updated = TZ.localize(datetime.now())
        visit.save()

        return visit


class Visit(models.Model):

    visit_state = models.ForeignKey(to=VisitState)

    last_updated = models.DateTimeField(null=False, blank=False, auto_now=True, db_index=True)

    objects = VisitManager()

    class Meta:
        db_table = 'visits'
        app_label = 'visit'

class VisitStateHistory(models.Model):

    visit = models.ForeignKey(to=Visit, related_name='visit_state_history')

    visit_state = models.ForeignKey(to=VisitState)

    time_created = models.DateTimeField()

    time_updated = models.DateTimeField()

    class Meta:
        db_table = 'visit_state_history'
        app_label = 'visit'


