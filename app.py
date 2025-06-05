import streamlit as st
import pandas as pd
import plotly.express as px
import datetime

st.set_page_config(layout='wide')
st.title("📊 Market Direction Indicator")

# Sample time series data
date_range = pd.date_range(start='2024-01-01', periods=100, freq='D')
assets = ['EUR/USD', 'SPX', 'AAPL', 'USD/JPY', 'DAX', 'TSLA']
asset_data = {
    asset: {
        "Date": date_range,
        "Fundamentals": pd.Series(range(50 + i, 150 + i)),
        "Sentiment": pd.Series(range(60 + i, 160 + i)),
        "Geopolitical Risk": pd.Series(range(30 + i, 130 + i))
    }
    for i, asset in enumerate(assets)
}

# Alerts logic
def show_alerts(df, asset):
    last = df.iloc[-1]
    if last['Fundamentals'] > 70:
        st.toast(f"📈 {asset} Fundamentals: {last['Fundamentals']} (Strong Bullish)", icon="✅")
        play_sound()
    if last['Sentiment'] < 30:
        st.toast(f"📉 {asset} Sentiment: {last['Sentiment']} (Strong Bearish)", icon="⚠️")
        play_sound()
    if last['Geopolitical Risk'] > 65:
        st.toast(f"⚠️ {asset} Geopolitical Risk: {last['Geopolitical Risk']} (High Tension)", icon="🚨")
        play_sound()

# Sound trigger using HTML/JS
def play_sound():
    sound_html = '''
    <audio autoplay>
        <source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg">
    </audio>
    '''
    st.markdown(sound_html, unsafe_allow_html=True)

# Chart rendering
tabs = st.tabs(assets)
for i, asset in enumerate(assets):
    with tabs[i]:
        st.subheader(f"{asset} Historical Data")
        df = pd.DataFrame(asset_data[asset])
        for metric in ['Fundamentals', 'Sentiment', 'Geopolitical Risk']:
            fig = px.line(df, x="Date", y=metric, title=f"{asset} - {metric}", template="plotly_dark")
            st.plotly_chart(fig, use_container_width=True)

        show_alerts(df, asset)

        # Log simulated score
        today = datetime.date.today().isoformat()
        latest_row = df.iloc[-1].to_frame().T
        latest_row.insert(0, "Asset", asset)
        latest_row.to_csv(f"history_{asset.replace('/', '')}.csv", mode='a', index=False, header=False)