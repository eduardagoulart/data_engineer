import pandas as pd
import sqlite3

df = pd.read_csv('finalapi.csv')
conn = sqlite3.connect('finalapi.db')
c = conn.cursor()


def check_nan(query):
    return query.isnull().sum().sum()


def create_sql():
    if check_nan(df) != 0:
        df.fillna(0)

    df.to_sql('Insurance', conn, if_exists='append', index=False)


if '__main__' == __name__:
    create_sql()
