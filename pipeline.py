from extract import fetch_all, INDICATORS
from transform import transform_all
from load import get_connection, create_table, load_data, DB_PATH

def run_pipeline():
    print("Starting ETL pipeline...")
    all_data = fetch_all(INDICATORS)
    combined_df = transform_all(all_data)

    conn = get_connection()
    create_table(conn)
    load_data(conn, combined_df)
    conn.close()

    print(f"Pipeline complete. Loaded {len(combined_df)} rows into {DB_PATH}")

if __name__ == "__main__":
    run_pipeline()
    