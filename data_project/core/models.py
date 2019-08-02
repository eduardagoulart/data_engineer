from django.db import models


class Insurance(models.Model):
    agency_id = models.IntegerField(db_column='AGENCY_ID', blank=True, null=True)  # Field name made lowercase.
    primary_agency_id = models.IntegerField(db_column='PRIMARY_AGENCY_ID', blank=True,
                                            null=True)  # Field name made lowercase.
    prod_abbr = models.TextField(db_column='PROD_ABBR', blank=True, null=True)  # Field name made lowercase.
    prod_line = models.TextField(db_column='PROD_LINE', blank=True, null=True)  # Field name made lowercase.
    state_abbr = models.TextField(db_column='STATE_ABBR', blank=True, null=True)  # Field name made lowercase.
    stat_profile_date_year = models.IntegerField(db_column='STAT_PROFILE_DATE_YEAR', blank=True,
                                                 null=True)  # Field name made lowercase.
    retention_poly_qty = models.IntegerField(db_column='RETENTION_POLY_QTY', blank=True,
                                             null=True)  # Field name made lowercase.
    poly_inforce_qty = models.IntegerField(db_column='POLY_INFORCE_QTY', blank=True,
                                           null=True)  # Field name made lowercase.
    prev_poly_inforce_qty = models.IntegerField(db_column='PREV_POLY_INFORCE_QTY', blank=True,
                                                null=True)  # Field name made lowercase.
    nb_wrtn_prem_amt = models.FloatField(db_column='NB_WRTN_PREM_AMT', blank=True,
                                         null=True)  # Field name made lowercase.
    wrtn_prem_amt = models.FloatField(db_column='WRTN_PREM_AMT', blank=True, null=True)  # Field name made lowercase.
    prev_wrtn_prem_amt = models.FloatField(db_column='PREV_WRTN_PREM_AMT', blank=True,
                                           null=True)  # Field name made lowercase.
    prd_ernd_prem_amt = models.FloatField(db_column='PRD_ERND_PREM_AMT', blank=True,
                                          null=True)  # Field name made lowercase.
    prd_incrd_losses_amt = models.FloatField(db_column='PRD_INCRD_LOSSES_AMT', blank=True,
                                             null=True)  # Field name made lowercase.
    months = models.IntegerField(db_column='MONTHS', blank=True, null=True)  # Field name made lowercase.
    retention_ratio = models.FloatField(db_column='RETENTION_RATIO', blank=True,
                                        null=True)  # Field name made lowercase.
    loss_ratio = models.FloatField(db_column='LOSS_RATIO', blank=True, null=True)  # Field name made lowercase.
    loss_ratio_3yr = models.FloatField(db_column='LOSS_RATIO_3YR', blank=True, null=True)  # Field name made lowercase.
    growth_rate_3yr = models.FloatField(db_column='GROWTH_RATE_3YR', blank=True,
                                        null=True)  # Field name made lowercase.
    agency_appointment_year = models.IntegerField(db_column='AGENCY_APPOINTMENT_YEAR', blank=True,
                                                  null=True)  # Field name made lowercase.
    active_producers = models.IntegerField(db_column='ACTIVE_PRODUCERS', blank=True,
                                           null=True)  # Field name made lowercase.
    max_age = models.IntegerField(db_column='MAX_AGE', blank=True, null=True)  # Field name made lowercase.
    min_age = models.IntegerField(db_column='MIN_AGE', blank=True, null=True)  # Field name made lowercase.
    vendor_ind = models.TextField(db_column='VENDOR_IND', blank=True, null=True)  # Field name made lowercase.
    vendor = models.TextField(db_column='VENDOR', blank=True, null=True)  # Field name made lowercase.
    pl_start_year = models.IntegerField(db_column='PL_START_YEAR', blank=True, null=True)  # Field name made lowercase.
    pl_end_year = models.IntegerField(db_column='PL_END_YEAR', blank=True, null=True)  # Field name made lowercase.
    commisions_start_year = models.IntegerField(db_column='COMMISIONS_START_YEAR', blank=True,
                                                null=True)  # Field name made lowercase.
    commisions_end_year = models.IntegerField(db_column='COMMISIONS_END_YEAR', blank=True,
                                              null=True)  # Field name made lowercase.
    cl_start_year = models.IntegerField(db_column='CL_START_YEAR', blank=True, null=True)  # Field name made lowercase.
    cl_end_year = models.IntegerField(db_column='CL_END_YEAR', blank=True, null=True)  # Field name made lowercase.
    activity_notes_start_year = models.IntegerField(db_column='ACTIVITY_NOTES_START_YEAR', blank=True,
                                                    null=True)  # Field name made lowercase.
    activity_notes_end_year = models.IntegerField(db_column='ACTIVITY_NOTES_END_YEAR', blank=True,
                                                  null=True)  # Field name made lowercase.
    cl_bound_ct_mds = models.IntegerField(db_column='CL_BOUND_CT_MDS', blank=True,
                                          null=True)  # Field name made lowercase.
    cl_quo_ct_mds = models.IntegerField(db_column='CL_QUO_CT_MDS', blank=True, null=True)  # Field name made lowercase.
    cl_bound_ct_sbz = models.IntegerField(db_column='CL_BOUND_CT_SBZ', blank=True,
                                          null=True)  # Field name made lowercase.
    cl_quo_ct_sbz = models.IntegerField(db_column='CL_QUO_CT_SBZ', blank=True, null=True)  # Field name made lowercase.
    cl_bound_ct_eqt = models.IntegerField(db_column='CL_BOUND_CT_eQT', blank=True,
                                          null=True)  # Field name made lowercase.
    cl_quo_ct_eqt = models.IntegerField(db_column='CL_QUO_CT_eQT', blank=True, null=True)  # Field name made lowercase.
    pl_bound_ct_elinks = models.IntegerField(db_column='PL_BOUND_CT_ELINKS', blank=True,
                                             null=True)  # Field name made lowercase.
    pl_quo_ct_elinks = models.IntegerField(db_column='PL_QUO_CT_ELINKS', blank=True,
                                           null=True)  # Field name made lowercase.
    pl_bound_ct_plrank = models.IntegerField(db_column='PL_BOUND_CT_PLRANK', blank=True,
                                             null=True)  # Field name made lowercase.
    pl_quo_ct_plrank = models.IntegerField(db_column='PL_QUO_CT_PLRANK', blank=True,
                                           null=True)  # Field name made lowercase.
    pl_bound_ct_eqtte = models.IntegerField(db_column='PL_BOUND_CT_eQTte', blank=True,
                                            null=True)  # Field name made lowercase.
    pl_quo_ct_eqtte = models.IntegerField(db_column='PL_QUO_CT_eQTte', blank=True,
                                          null=True)  # Field name made lowercase.
    pl_bound_ct_applied = models.IntegerField(db_column='PL_BOUND_CT_APPLIED', blank=True,
                                              null=True)  # Field name made lowercase.
    pl_quo_ct_applied = models.IntegerField(db_column='PL_QUO_CT_APPLIED', blank=True,
                                            null=True)  # Field name made lowercase.
    pl_bound_ct_transactnow = models.IntegerField(db_column='PL_BOUND_CT_TRANSACTNOW', blank=True,
                                                  null=True)  # Field name made lowercase.
    pl_quo_ct_transactnow = models.IntegerField(db_column='PL_QUO_CT_TRANSACTNOW', blank=True,
                                                null=True)  # Field name made lowercase.

    def __str__(self):
        return self.vendor
