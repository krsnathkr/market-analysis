# app.py
import streamlit as st
from google_gemini_api import configure_gemini, generate_financial_analysis

configure_gemini()

st.title("Stock Market Analysis Tool :moneybag:")
st.write("The Market Analysis Tool is an innovative web application designed to assist investors, business owners, and financial enthusiasts in analyzing market trends and gaining insights from financial data and news. Utilizing the powerful Google Generative AI API, this tool provides detailed summaries, data analysis, and investment strategy explanations, all tailored to specific queries.")
st.write("---")

st.sidebar.header("Query Parameters")
query = st.sidebar.text_input("Search Query", value="Micron - MU")

if st.sidebar.button("Fetch Data"):
    data = generate_financial_analysis(query)
    if data:
        st.write("### Financial Analysis and Insights")
        st.write(data)
    else:
        st.write("No data found or API error.")
