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
        generic_request = self.request.query_params.get(list(self.request.query_params.keys())[0], None)

        if generic_request is not None:
            if list(self.request.query_params.keys())[0] == 'months':
                queryset = queryset.filter(months=generic_request)
            elif list(self.request.query_params.keys())[0] == 'state_abbr':
                queryset = queryset.filter(state_abbr=generic_request)
            elif list(self.request.query_params.keys())[0] == 'agency_id':
                queryset = queryset.filter(agency_id=generic_request)
            elif list(self.request.query_params.keys())[0] == 'stat_profile_date_year':
                queryset = queryset.filter(stat_profile_date_year=generic_request)
        return queryset
