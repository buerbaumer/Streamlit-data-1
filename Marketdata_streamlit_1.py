import yfinance as yf
import streamlit as st

st.write("""
# Hallo Blockstar!

Shown are closing price and volume data:

""")

#define the ticker symbol
tickerSymbol_def = 'ETH-USD'
tickerSymbol = st.text_input("Ticker Symbol:", tickerSymbol_def)
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
#tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2022-10-23')
tickerDf = tickerData.history(period='max')

st.write('ShortName:           ', tickerData.info['shortName'])
st.write('Symbol:              ', tickerData.info['symbol'])
st.write('RegularMarketPrice:  ', tickerData.info['regularMarketPrice'])
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")

st.line_chart(tickerDf.Close)

st.write("""
## Volume
""")

st.line_chart(tickerDf.Volume)
