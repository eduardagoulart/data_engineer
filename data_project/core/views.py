from rest_framework import generics
from rest_framework import viewsets

from data_project.core.models import Insurance
from data_project.core.serializers import InsuranceSerializer


class InsuranceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer


class PurchaseList(generics.ListAPIView):
    serializer_class = InsuranceSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Insurance.objects.all()
        username = self.request.query_params.get('state_abbr', None)
        if username is not None:
            queryset = queryset.filter(months=username)
        return queryset
