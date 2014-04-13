from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from src.apps.visit.models import Visit
import simplejson as json


def update(request, visit_id, visit_state_id):
    print "Visit: %s, visit state id: %s" % (visit_id, visit_state_id)

    visit = Visit.objects.update_visit(visit_id, visit_state_id)

    return HttpResponse(json.dumps(model_to_dict(visit)), content_type="application/json")

