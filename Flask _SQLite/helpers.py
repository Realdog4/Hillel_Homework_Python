import sqlite3

DATABASE = 'chinook.db'


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def connection_to_database():
    conn = get_db_connection()
    cursor = conn.cursor()
    return cursor

