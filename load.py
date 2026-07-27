import sqlite3

DB_PATH = "econ_indicators.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn

def create_table(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS indicators (
            date TEXT,
            value REAL,
            indicator TEXT
        )
    """)
    conn.commit

def load_data(conn, df):
    df.to_sql('indicators', conn, if_exists='replace', index=False)

if __name__ == "__main__":
    from transform import transform_all
    from extract import fetch_all, INDICATORS

    all_data = fetch_all(INDICATORS)
    combined_df = transform_all(all_data)

    conn = get_connection()
    create_table(conn)
    load_data(conn, combined_df)
    conn.close()

    print(f"Loaded {len(combined_df)} rows into {DB_PATH}")