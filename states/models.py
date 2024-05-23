from django.db import models

class State(models.Model):
    name = models.CharField(max_length=200)
    identifier = models.CharField(max_length=100)
#    containedInPlace = models.Place()
#    containsPlace = models.Place()
    url = models.URLField( 
                  max_length = 200, 
                )