
# cot_fetcher.py
import pandas as pd

def fetch_cot_sample():
    # Placeholder for live scraping or weekly update from CFTC
    # In production, replace with dynamic file load or API call
    data = {
        "Asset": ["EUR/USD", "GBP/USD", "SPX", "XAU/USD"],
        "Net Positions": [120000, 80000, -50000, 60000],
        "Change from Last Week": [5000, -2000, -3000, 4000],
        "Sentiment Score": [65, 60, 45, 70],
    }
    return pd.DataFrame(data)
