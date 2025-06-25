import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(layout='wide')
st.title('📈 Live Stock Dashboard')

tickers = ['AAPL', 'VOO', 'VTI', 'SPY', 'VGT', 'QQQ']
intervals = {'7D': '7d', '1M': '1mo', '1Y': '1y'}

selected_ticker = st.selectbox('Select a stock', tickers)
selected_interval = st.radio('Select period', list(intervals.keys()), horizontal=True)

# Fetch data
ticker_data = yf.Ticker(selected_ticker)
history = ticker_data.history(period=intervals[selected_interval])

if not history.empty:
    current_price = history['Close'].iloc[-1]
    price_change = current_price - history['Close'].iloc[0]
    percent_change = (price_change / history['Close'].iloc[0]) * 100
    
    price_color = 'green' if price_change > 0 else 'red' if price_change < 0 else 'gray'
    st.metric(
        label=f'{selected_ticker} Price',
        value=f'${current_price:.2f}',
        delta=f'{price_change:+.2f} ({percent_change:+.2f}%)',
        delta_color='normal' if price_change == 0 else ('inverse' if price_change < 0 else 'off'),
    )
    st.markdown(f'<span style="color:{price_color}; font-size: 18px;">{"▲" if price_change > 0 else "▼" if price_change < 0 else "■"} {price_change:+.2f} ({percent_change:+.2f}%)</span>', unsafe_allow_html=True)
    
    # Chart
    st.line_chart(history['Close'])
else:
    st.warning('No data available for this period.')

# Auto-refresh every 30 seconds
if 'last_refresh' not in st.session_state:
    st.session_state['last_refresh'] = datetime.now()
if datetime.now() - st.session_state['last_refresh'] > timedelta(seconds=30):
    st.session_state['last_refresh'] = datetime.now()
    st.rerun()
