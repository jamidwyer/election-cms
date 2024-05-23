from django.db import models
from states.models import State

class Candidate(models.Model):
#    affiliation = models.ManyToManyField(Organization)
#    alumniOf = models.ManyToManyField(Organization)
    birthPlace = State()
    email = models.CharField(max_length=200)
    familyName = models.CharField(max_length=200)
    givenName = models.CharField(max_length=200)
    honorificPrefix = models.CharField(max_length=200)
    honorificSuffix = models.CharField(max_length=200)
    jobTitle = models.CharField(max_length=200)
    #hasCredential
    #hasOccupation
#    funder = models.ManyToManyField(Organization)
#   memberOf = models.ManyToManyField(Organization)
#   worksFor = models.ManyToManyField(Organization)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    location = models.ManyToManyField(State)
    # eventSchedule
    # organizer = models.Organization()
    # issuePosition = additionalType?
    # subEvent
    # superEvent
    name = models.CharField(max_length=200)
    url = models.URLField( 
                  max_length = 200, 
                )
    #potentialAction
