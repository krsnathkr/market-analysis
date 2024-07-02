# app.py
import streamlit as st
import os
import plotly.express as px
import pandas as pd
from google_gemini_api import configure_gemini, generate_financial_analysis, fetch_stock_data

st.set_page_config(page_title="Market Radar", layout="wide")
st.title("Market Radar :chart_with_upwards_trend:")

st.sidebar.header("Query Parameters")
api_key = st.sidebar.text_input("Enter Google Gemini API Key", type="password")
ticker = st.sidebar.text_input("Enter Stock Ticker", value="MU")

if st.sidebar.button("Fetch Data"):
    if not api_key:
        st.sidebar.error("Please enter a valid API key.")
    elif not ticker:
        st.sidebar.error("Please enter a valid stock ticker.")
    else:
        with st.spinner("Fetching data..."):
            try:
                configure_gemini(api_key)
                data = generate_financial_analysis(ticker)
                stock_data = fetch_stock_data(ticker)
                
                if data:
                    st.subheader("Financial Analysis and Insights")
                    st.write(data)
                    st.write("---")
                    
                    if not stock_data.empty:
                        st.subheader(f"{ticker} Stock Price Data")
                        fig = px.line(stock_data, x=stock_data.index, y="Close", title=f"{ticker} Stock Prices Over the Last Year")
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        st.warning("No stock data found.")
                else:
                    st.error("No data found or API error.")
            except Exception as e:
                st.error(f"An error occurred: {e}")


st.sidebar.write("---")

st.sidebar.write("Get yourself a Google Gemini API key at https://aistudio.google.com/") 
st.sidebar.write("Developed by Krishna Thakar :heart:")
