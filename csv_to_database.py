import pandas as pd
import sqlite3

df = pd.read_csv('finalapi.csv')


def check_nan(query):
    return query.isnull().sum().sum()


def create_sql():
    types_query = [type(df_serie[0]) for df_serie in df]
    if check_nan(df) != 0:
        df.fillna(0)
    


create_sql()
