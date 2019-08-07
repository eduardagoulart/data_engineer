import sqlite3
import pandas as pd

df = pd.read_csv('finalapi.csv')
conn = sqlite3.connect('finalapi.sqlite3')
c = conn.cursor()
print(c)


def check_nan(query):
    return query.isnull().sum().sum()


def create_sql():
    if check_nan(df) != 0:
        df.fillna(0)

    df.to_sql('core_insurance', conn, if_exists='append', index=False)


def group_by_months(dataframe):
    data = dataframe.drop(
        ['AGENCY_ID', 'STATE_ABBR', 'STAT_PROFILE_DATE_YEAR'], axis=1)
    months = sorted(data['MONTHS'].drop_duplicates().tolist())
    data = data.groupby('MONTHS').sum()
    data['MONTHS'] = months
    data.to_sql('core_months', conn, if_exists='append', index=False)


def group_by_agency_id(dataframe):
    data = dataframe.drop(
        ['MONTHS', 'STATE_ABBR', 'STAT_PROFILE_DATE_YEAR'], axis=1)
    ids = data['AGENCY_ID'].drop_duplicates().tolist()
    data = data.groupby(['AGENCY_ID']).sum()
    data['AGENCY_ID'] = ids
    data.to_sql('core_agencyid', conn, if_exists='append', index=False)


def group_by_years(dataframe):
    data = dataframe.drop(['MONTHS', 'STATE_ABBR', 'AGENCY_ID'], axis=1)
    years = sorted(data['STAT_PROFILE_DATE_YEAR'].drop_duplicates().tolist())
    data = data.groupby(['STAT_PROFILE_DATE_YEAR']).sum()
    data['STAT_PROFILE_DATE_YEAR'] = years
    data.to_sql('core_year', conn, if_exists='append', index=False)


def group_by_state_abber(dataframe):
    data = dataframe.drop(
        ['MONTHS', 'STAT_PROFILE_DATE_YEAR', 'AGENCY_ID'], axis=1)
    state = sorted(data['STATE_ABBR'].drop_duplicates().tolist())
    data = data.groupby(['STATE_ABBR']).sum()
    data['STATE_ABBR'] = state
    data.to_sql('core_state', conn, if_exists='append', index=False)


def run():
    create_sql()
    dataframe = df.drop(['PRIMARY_AGENCY_ID', 'PROD_ABBR', 'PROD_LINE', 'RETENTION_POLY_QTY', 'POLY_INFORCE_QTY',
                         'PREV_POLY_INFORCE_QTY', 'NB_WRTN_PREM_AMT', 'WRTN_PREM_AMT', 'PREV_WRTN_PREM_AMT',
                         'RETENTION_RATIO', 'LOSS_RATIO', 'LOSS_RATIO_3YR', 'GROWTH_RATE_3YR',
                         'AGENCY_APPOINTMENT_YEAR', 'ACTIVE_PRODUCERS', 'MAX_AGE', 'MIN_AGE',
                         'VENDOR_IND', 'VENDOR', 'PL_START_YEAR', 'PL_END_YEAR', 'COMMISIONS_START_YEAR',
                         'COMMISIONS_END_YEAR', 'CL_START_YEAR', 'CL_END_YEAR', 'ACTIVITY_NOTES_START_YEAR',
                         'ACTIVITY_NOTES_END_YEAR', 'CL_BOUND_CT_MDS', 'CL_QUO_CT_MDS', 'CL_BOUND_CT_SBZ',
                         'CL_QUO_CT_SBZ',
                         'CL_BOUND_CT_eQT', 'CL_QUO_CT_eQT', 'PL_BOUND_CT_ELINKS', 'PL_QUO_CT_ELINKS',
                         'PL_BOUND_CT_PLRANK',
                         'PL_QUO_CT_PLRANK', 'PL_BOUND_CT_eQTte', 'PL_QUO_CT_eQTte', 'PL_BOUND_CT_APPLIED',
                         'PL_QUO_CT_APPLIED', 'PL_BOUND_CT_TRANSACTNOW', 'PL_QUO_CT_TRANSACTNOW'], axis=1)
    group_by_months(dataframe)
    group_by_agency_id(dataframe)
    group_by_years(dataframe)
    group_by_state_abber(dataframe)


if '__main__' == __name__:
    run()
