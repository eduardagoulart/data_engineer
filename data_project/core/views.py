from data_project.core.models import Insurance
from rest_framework import viewsets
from data_project.core.serializers import InsuranceSerializer


class InsuranceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
