import sqlite3

DB_PATH = "econ_indicators.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn

def create_table(conn):
    pass