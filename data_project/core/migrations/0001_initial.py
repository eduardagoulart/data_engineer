# Generated by Django 2.1.1 on 2019-08-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgencyId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prd_ernd_prem_amt', models.FloatField(blank=True, db_column='PRD_ERND_PREM_AMT', null=True)),
                ('prd_incrd_losses_amt', models.FloatField(blank=True, db_column='PRD_INCRD_LOSSES_AMT', null=True)),
                ('agency_id', models.IntegerField(blank=True, db_column='AGENCY_ID', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency_id', models.IntegerField(blank=True, db_column='AGENCY_ID', null=True)),
                ('primary_agency_id', models.IntegerField(blank=True, db_column='PRIMARY_AGENCY_ID', null=True)),
                ('prod_abbr', models.TextField(blank=True, db_column='PROD_ABBR', null=True)),
                ('prod_line', models.TextField(blank=True, db_column='PROD_LINE', null=True)),
                ('state_abbr', models.TextField(blank=True, db_column='STATE_ABBR', null=True)),
                ('stat_profile_date_year', models.IntegerField(blank=True, db_column='STAT_PROFILE_DATE_YEAR', null=True)),
                ('retention_poly_qty', models.IntegerField(blank=True, db_column='RETENTION_POLY_QTY', null=True)),
                ('poly_inforce_qty', models.IntegerField(blank=True, db_column='POLY_INFORCE_QTY', null=True)),
                ('prev_poly_inforce_qty', models.IntegerField(blank=True, db_column='PREV_POLY_INFORCE_QTY', null=True)),
                ('nb_wrtn_prem_amt', models.FloatField(blank=True, db_column='NB_WRTN_PREM_AMT', null=True)),
                ('wrtn_prem_amt', models.FloatField(blank=True, db_column='WRTN_PREM_AMT', null=True)),
                ('prev_wrtn_prem_amt', models.FloatField(blank=True, db_column='PREV_WRTN_PREM_AMT', null=True)),
                ('prd_ernd_prem_amt', models.FloatField(blank=True, db_column='PRD_ERND_PREM_AMT', null=True)),
                ('prd_incrd_losses_amt', models.FloatField(blank=True, db_column='PRD_INCRD_LOSSES_AMT', null=True)),
                ('months', models.IntegerField(blank=True, db_column='MONTHS', null=True)),
                ('retention_ratio', models.FloatField(blank=True, db_column='RETENTION_RATIO', null=True)),
                ('loss_ratio', models.FloatField(blank=True, db_column='LOSS_RATIO', null=True)),
                ('loss_ratio_3yr', models.FloatField(blank=True, db_column='LOSS_RATIO_3YR', null=True)),
                ('growth_rate_3yr', models.FloatField(blank=True, db_column='GROWTH_RATE_3YR', null=True)),
                ('agency_appointment_year', models.IntegerField(blank=True, db_column='AGENCY_APPOINTMENT_YEAR', null=True)),
                ('active_producers', models.IntegerField(blank=True, db_column='ACTIVE_PRODUCERS', null=True)),
                ('max_age', models.IntegerField(blank=True, db_column='MAX_AGE', null=True)),
                ('min_age', models.IntegerField(blank=True, db_column='MIN_AGE', null=True)),
                ('vendor_ind', models.TextField(blank=True, db_column='VENDOR_IND', null=True)),
                ('vendor', models.TextField(blank=True, db_column='VENDOR', null=True)),
                ('pl_start_year', models.IntegerField(blank=True, db_column='PL_START_YEAR', null=True)),
                ('pl_end_year', models.IntegerField(blank=True, db_column='PL_END_YEAR', null=True)),
                ('commisions_start_year', models.IntegerField(blank=True, db_column='COMMISIONS_START_YEAR', null=True)),
                ('commisions_end_year', models.IntegerField(blank=True, db_column='COMMISIONS_END_YEAR', null=True)),
                ('cl_start_year', models.IntegerField(blank=True, db_column='CL_START_YEAR', null=True)),
                ('cl_end_year', models.IntegerField(blank=True, db_column='CL_END_YEAR', null=True)),
                ('activity_notes_start_year', models.IntegerField(blank=True, db_column='ACTIVITY_NOTES_START_YEAR', null=True)),
                ('activity_notes_end_year', models.IntegerField(blank=True, db_column='ACTIVITY_NOTES_END_YEAR', null=True)),
                ('cl_bound_ct_mds', models.IntegerField(blank=True, db_column='CL_BOUND_CT_MDS', null=True)),
                ('cl_quo_ct_mds', models.IntegerField(blank=True, db_column='CL_QUO_CT_MDS', null=True)),
                ('cl_bound_ct_sbz', models.IntegerField(blank=True, db_column='CL_BOUND_CT_SBZ', null=True)),
                ('cl_quo_ct_sbz', models.IntegerField(blank=True, db_column='CL_QUO_CT_SBZ', null=True)),
                ('cl_bound_ct_eqt', models.IntegerField(blank=True, db_column='CL_BOUND_CT_eQT', null=True)),
                ('cl_quo_ct_eqt', models.IntegerField(blank=True, db_column='CL_QUO_CT_eQT', null=True)),
                ('pl_bound_ct_elinks', models.IntegerField(blank=True, db_column='PL_BOUND_CT_ELINKS', null=True)),
                ('pl_quo_ct_elinks', models.IntegerField(blank=True, db_column='PL_QUO_CT_ELINKS', null=True)),
                ('pl_bound_ct_plrank', models.IntegerField(blank=True, db_column='PL_BOUND_CT_PLRANK', null=True)),
                ('pl_quo_ct_plrank', models.IntegerField(blank=True, db_column='PL_QUO_CT_PLRANK', null=True)),
                ('pl_bound_ct_eqtte', models.IntegerField(blank=True, db_column='PL_BOUND_CT_eQTte', null=True)),
                ('pl_quo_ct_eqtte', models.IntegerField(blank=True, db_column='PL_QUO_CT_eQTte', null=True)),
                ('pl_bound_ct_applied', models.IntegerField(blank=True, db_column='PL_BOUND_CT_APPLIED', null=True)),
                ('pl_quo_ct_applied', models.IntegerField(blank=True, db_column='PL_QUO_CT_APPLIED', null=True)),
                ('pl_bound_ct_transactnow', models.IntegerField(blank=True, db_column='PL_BOUND_CT_TRANSACTNOW', null=True)),
                ('pl_quo_ct_transactnow', models.IntegerField(blank=True, db_column='PL_QUO_CT_TRANSACTNOW', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Months',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prd_ernd_prem_amt', models.FloatField(blank=True, db_column='PRD_ERND_PREM_AMT', null=True)),
                ('prd_incrd_losses_amt', models.FloatField(blank=True, db_column='PRD_INCRD_LOSSES_AMT', null=True)),
                ('months', models.IntegerField(blank=True, db_column='MONTHS', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prd_ernd_prem_amt', models.FloatField(blank=True, db_column='PRD_ERND_PREM_AMT', null=True)),
                ('prd_incrd_losses_amt', models.FloatField(blank=True, db_column='PRD_INCRD_LOSSES_AMT', null=True)),
                ('state_abbr', models.TextField(blank=True, db_column='STATE_ABBR', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prd_ernd_prem_amt', models.FloatField(blank=True, db_column='PRD_ERND_PREM_AMT', null=True)),
                ('prd_incrd_losses_amt', models.FloatField(blank=True, db_column='PRD_INCRD_LOSSES_AMT', null=True)),
                ('stat_profile_date_year', models.IntegerField(blank=True, db_column='STAT_PROFILE_DATE_YEAR', null=True)),
            ],
        ),
    ]
