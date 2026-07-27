# Econ Indicators ETL

A Python ETL pipeline that extracts key U.S. macroeconomic indicators from the FRED (Federal Reserve Economic Data) API, transforms them into a tidy long-format table, and loads them into a local SQLite database for analysis.

## Indicators Tracked
- **GDP** — Gross Domestic Product (quarterly)
- **CPIAUCSL** — Consumer Price Index (monthly)
- **UNRATE** — Unemployment Rate (monthly)
- **FEDFUNDS** — Federal Funds Rate (monthly)
- **DGS10** — 10-Year Treasury Yield (daily)

## Pipeline
1. **Extract** (`extract.py`) — pulls each series from the FRED API via `fredapi`
2. **Transform** (`transform.py`) — reshapes each series into a long-format table (`date | value | indicator`) and combines all indicators into one DataFrame
3. **Load** (`load.py`) — writes the combined data into a SQLite database (`econ_indicators.db`)

## Usage
```bash
pip install -r requirements.txt
# create a .env file with FRED_API_KEY=your_key_here
python pipeline.py
```

## Tech Stack
Python, pandas, fredapi, SQLite

## Example Query
```python
import sqlite3
conn = sqlite3.connect("econ_indicators.db")
cursor = conn.execute("SELECT indicator, COUNT(*) FROM indicators GROUP BY indicator")
print(cursor.fetchall())
```