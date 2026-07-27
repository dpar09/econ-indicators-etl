from fredapi import Fred
from dotenv import load_dotenv
import os

load_dotenv()
fred = Fred(api_key=os.getenv("FRED_API_KEY"))

def fetch_indicator(series_id):
    data = fred.get_series(series_id)
    return data

INDICATORS = {
    "GDP" : "Gross Domestic Product",
    "CPIAUCSL" : "Consumer Price Index",
    "UNRATE" : "Unemployment Rate",
    "FEDFUNDS" : "Federal Funds Rate",
    "DGS10" : "10-Year Treasury Yield"
}

def fetch_all(indicators):
    results = {}
    for series_id in indicators:
        print(f"Fetching {series_id}...")
        results[series_id] = fetch_indicator(series_id)
    return results

if __name__ == "__main__":
    all_data = fetch_all(INDICATORS)
    print(all_data.keys())
    print(all_data["UNRATE"].tail())