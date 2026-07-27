import sqlite3
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

