
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Market Direction Indicator", layout="wide")

st.title("📈 Market Direction Indicator")
st.markdown("A real-time sentiment + fundamentals dashboard. Powered by FRED, COT, and live geopolitical insights.")

# Assets and example live scores (to be replaced with real-time fetch)
assets = [
    "EUR/USD", "SPX", "AAPL", "GBP/USD", "XAU/USD", "USOIL", "USTECH 100"
]

# Placeholder logic simulating score fetching (replace later with FRED/COT APIs)
def simulate_score():
    return np.random.randint(30, 90)

data = []
for asset in assets:
    fundamental = simulate_score()
    sentiment = simulate_score()
    geopolitics = simulate_score()
    data.append([asset, fundamental, sentiment, geopolitics])

df = pd.DataFrame(data, columns=["Asset", "Fundamental Score", "Sentiment Score", "Geopolitical Risk"])

# Styling logic for color-coded cells
def color_score(val, category):
    if category in ["Fundamental Score", "Sentiment Score"]:
        if val >= 75:
            return 'background-color: darkgreen; color: white'
        elif val >= 60:
            return 'background-color: green; color: white'
        elif val >= 45:
            return 'background-color: lightgreen; color: black'
        else:
            return 'background-color: lightblue; color: black'
    elif category == "Geopolitical Risk":
        if val >= 70:
            return 'background-color: red; color: white'
        elif val >= 50:
            return 'background-color: orange; color: black'
        elif val >= 30:
            return 'background-color: yellow; color: black'
        else:
            return 'background-color: lightblue; color: black'
    return ''

# Apply styling
styled_df = df.style.applymap(lambda val: color_score(val, "Fundamental Score"), subset=["Fundamental Score"])
styled_df = styled_df.applymap(lambda val: color_score(val, "Sentiment Score"), subset=["Sentiment Score"])
styled_df = styled_df.applymap(lambda val: color_score(val, "Geopolitical Risk"), subset=["Geopolitical Risk"])

st.dataframe(styled_df, use_container_width=True)

st.markdown("---")
st.markdown("📡 Live integrations (FRED, COT, News) loading next...")

