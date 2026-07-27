import pandas as pd
from extract import fetch_indicator

def transform_indicator(series, series_id):
    df = series.reset_index()
    df.columns = ["date", "value"]
    df["indicator"] = series_id
    return df

from extract import fetch_all, INDICATORS

def transform_all(all_data):
    frames = []
    for series_id, series in all_data.items():
        df = transform_indicator(series, series_id)
        frames.append(df)
    combined = pd.concat(frames, ignore_index=True)
    return combined

if __name__ == "__main__":
    all_data = fetch_all(INDICATORS)
    combined_df = transform_all(all_data)
    print(combined_df.shape)
    print(combined_df.head())
    print(combined_df["indicator"].unique())