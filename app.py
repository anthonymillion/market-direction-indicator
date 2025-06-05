
import streamlit as st
import pandas as pd
import numpy as np

from fred_fetcher import get_fred_series
from cot_fetcher import fetch_cot_sample
from news_fetcher import fetch_rss_headlines

st.set_page_config(page_title="Market Direction Indicator", layout="wide")
st.title("📈 Market Direction Indicator")
st.markdown("Live dashboard with fundamentals, sentiment, and geopolitical insights.")

# === Section 1: Fundamentals ===
st.header("📊 Fundamentals (FRED)")

try:
    fed_funds = get_fred_series("FEDFUNDS")
    latest_rate = fed_funds['value'].iloc[-1]
    st.metric("Federal Funds Rate (Latest)", f"{latest_rate:.2f}%")
    st.line_chart(fed_funds.set_index('date')['value'], height=200)
except Exception as e:
    st.error(f"Failed to fetch FRED data: {e}")

# === Section 2: Sentiment (COT) ===
st.header("💬 COT Sentiment Scores")

try:
    cot_df = fetch_cot_sample()
    st.dataframe(cot_df, use_container_width=True)
except Exception as e:
    st.error(f"Failed to fetch COT sentiment data: {e}")

# === Section 3: Geopolitical News ===
st.header("🌍 Geopolitical & Market News")

try:
    news_df = fetch_rss_headlines()
    for index, row in news_df.iterrows():
        st.markdown(f"- [{row['title']}]({row['link']}) — *{row['published']}*")
except Exception as e:
    st.error(f"Failed to fetch news headlines: {e}")

st.markdown("---")
st.markdown("✅ Live integrations from **FRED**, **COT**, and **ForexFactory RSS** are now active.")
