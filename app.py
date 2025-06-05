
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Market Direction Indicator", layout="wide")

st.title("📈 Market Direction Indicator")

st.markdown("""
This is a prototype for tracking market direction using a blend of:
- 📊 **Fundamentals**
- 💬 **Sentiment**
- 🌍 **Geopolitical events**

Initial assets tracked:
- EUR/USD
- SPX (S&P 500)
- AAPL
- GBP/USD
- XAU/USD (Gold)
- USOIL (WTI Crude)
- USTECH 100 (NASDAQ)

Coming soon: Live data integrations, scoring system, and visual indicators.
""")

# Sample placeholder data
data = {
    "Asset": ["EUR/USD", "SPX", "AAPL", "GBP/USD", "XAU/USD", "USOIL", "USTECH 100"],
    "Fundamental Score": [65, 80, 75, 60, 70, 55, 78],
    "Sentiment Score": [50, 85, 77, 45, 67, 53, 81],
    "Geopolitical Risk": [20, 10, 15, 25, 30, 35, 12]
}
df = pd.DataFrame(data)

st.dataframe(df)

st.markdown("---")
st.markdown("🔧 **Note:** This is an MVP. Scores are static for now — live feeds from FRED, COT, and news coming soon!")
