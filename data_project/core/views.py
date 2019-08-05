from rest_framework import generics
from rest_framework import viewsets
from rest_pandas import PandasView, PandasCSVRenderer

from data_project.core.models import Insurance
from data_project.core.serializers import InsuranceSerializer


class InsuranceViewSet(viewsets.ModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer


class PurchaseList(generics.ListAPIView):
    serializer_class = InsuranceSerializer

    def get_queryset(self):
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


class TimeSeriesView(PandasView):
    queryset = Insurance.objects.all()

    def filter_queryset(self, queryset):
        queryset = Insurance.objects.all()
        generic_queryset = self.request.query_params.get('data', None)

        if generic_queryset is not None:
            queryset = queryset.filter(stat_profile_date_year=generic_queryset)
        return queryset

    serializer_class = InsuranceSerializer

    def transform_dataframe(self, dataframe):
        dataframe = dataframe.drop(
            ['primary_agency_id', 'prod_abbr', 'state_abbr', 'stat_profile_date_year', 'retention_poly_qty',
             'poly_inforce_qty', 'prev_poly_inforce_qty', 'nb_wrtn_prem_amt', 'wrtn_prem_amt', 'prev_wrtn_prem_amt',
             'prd_ernd_prem_amt', 'prd_incrd_losses_amt', 'months', 'retention_ratio', 'loss_ratio', 'loss_ratio_3yr',
             'growth_rate_3yr', 'agency_appointment_year', 'active_producers', 'max_age', 'min_age', 'vendor_ind',
             'vendor', 'pl_start_year', 'pl_end_year', 'commisions_start_year', 'commisions_end_year', 'cl_start_year',
             'cl_end_year', 'activity_notes_start_year', 'activity_notes_end_year', 'cl_bound_ct_mds', 'cl_quo_ct_mds',
             'cl_bound_ct_sbz', 'cl_quo_ct_sbz', 'cl_bound_ct_eqt', 'cl_quo_ct_eqt', 'pl_bound_ct_elinks',
             'pl_quo_ct_elinks', 'pl_bound_ct_plrank', 'pl_quo_ct_plrank', 'pl_bound_ct_eqtte', 'pl_quo_ct_eqtte',
             'pl_bound_ct_applied', 'pl_quo_ct_applied', 'pl_bound_ct_transactnow', 'pl_quo_ct_transactnow'], axis=1)

        return dataframe

    renderer_classes = [PandasCSVRenderer]

    def get_pandas_filename(self, request, format):
        if format in ('csv', 'xls', 'xlsx'):
            return "report_data"
        else:
            return None
