import yfinance as yf
import streamlit as st

st.write("""
# Simple Marketdata Price App

Shown are ETHEREUM closing price and volume of ...

""")

#define the ticker symbol
tickerSymbol = 'ETH-USD'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-12-16')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
