from django.db import models


class VisitState(models.Model):
    
    state = models.CharField(max_length=255, null=False, blank=False)
    

class VisitStateHistory(models.Model):

    visit_state = models.ForeignKey(to=VisitState)

    datetime_created = models.DateTimeField()

    datetime_updated = models.DateTimeField()


class Visit(models.Model):

    visit_state = models.ForeignKey(to=VisitState)

    visit_state_history = models.ForeignKey(to=VisitStateHistory)

    last_updated = models.DateTimeField(null=False, blank=False, auto_now=True)


