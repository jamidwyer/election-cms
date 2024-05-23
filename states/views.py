from rest_framework import viewsets
from candidates.models import Candidate
from events.models import Event
from states.models import State
from states.serializers import StateSerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer