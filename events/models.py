from django.db import models
from candidates.models import Candidate
from states.models import State

class Event(models.Model):
    candidate = models.ManyToManyField(Candidate)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    location = models.ManyToManyField(State)
    # eventSchedule
    # organizer = models.Organization()
    # subEvent
    # superEvent
    name = models.CharField(max_length=200)
    url = models.URLField( 
                  max_length = 200, 
                )
    #potentialAction
