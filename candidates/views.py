from rest_framework import viewsets
from candidates.models import Candidate
from candidates.serializers import CandidateSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
