import sqlite3
import pandas as pd
from src.sql import sqlite_queries

def connect_database(database_path):
    connection = sqlite3.connect(database_path)
    return connection

def close_database(connection):
    connection.close()

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute(sqlite_queries.CREATE_TRANSACTIONS_TABLE)
    connection.commit()


def adapt_sqlite_value(value): #Convierte tipos de pandas a tipos compatibles con SQLitegit
    if pd.isna(value):
        return None

    if isinstance(value,pd.Timestamp):
        return value.date().isoformat()

    return value


def insert_dataframe(connection,df):
    cursor = connection.cursor()
    for _, row in df.iterrows(): # Para optimizar itertuples()
        cursor.execute(
        sqlite_queries.INSERT_DATAFRAME,
         (
            adapt_sqlite_value(row["id"]),
            adapt_sqlite_value(row["fecha"]),
            adapt_sqlite_value(row["tipo"]),
            adapt_sqlite_value(row["categoria"]),
            adapt_sqlite_value(row["descripcion"]),
            adapt_sqlite_value(row["monto"]),
            adapt_sqlite_value(row["modo_pago"])
        )
)
    connection.commit()

def read_database(connection):
    return pd.read_sql_query(sqlite_queries.READ_PERSONAL_FINANCE,connection)

def clear_table(connection):
    cursor = connection.cursor()
    cursor.execute(sqlite_queries.DELETE_TABLE)
    connection.commit()
