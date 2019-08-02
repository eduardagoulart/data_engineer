import sqlite3
import pandas as pd

df = pd.read_csv('finalapi.csv')
conn = sqlite3.connect('finalapi.sqlite3')
c = conn.cursor()


def check_nan(query):
    return query.isnull().sum().sum()


def create_sql():
    if check_nan(df) != 0:
        df.fillna(0)

    df.to_sql('core_insurance', conn, if_exists='append', index=False)


if '__main__' == __name__:
    create_sql()
