
# fred_fetcher.py
import requests
import pandas as pd
import os

FRED_API_KEY = os.getenv("FRED_API_KEY", "YOUR_FRED_API_KEY")

def get_fred_series(series_id, start_date="2022-01-01"):
    url = f"https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "observation_start": start_date,
    }
    response = requests.get(url, params=params)
    data = response.json()
    df = pd.DataFrame(data["observations"])
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    return df[["date", "value"]]
