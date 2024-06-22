# google_gemini_api.py
import os
import yfinance as yf
import google.generativeai as genai

def configure_gemini(api_key):
    if not api_key:
        raise ValueError("API key not provided.")
    genai.configure(api_key=api_key)

def generate_financial_analysis(query):
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    prompt = (
        f"input: Provide detailed information about the stock {query}. Please include the following:\n"
        "Key financials (revenue, net income, EPS, etc.)\n"
        "Major recent news and updates\n"
        "Analyst ratings and target prices\n"
        "Investment strategy insights (growth potential, risks, expert opinions, etc.)\n"
        "Please format the response with bullet points for clarity.\n"
    )

    response = model.generate_content([prompt, "output: "])

    return response.text if response else None

def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1y")
    return hist                              
