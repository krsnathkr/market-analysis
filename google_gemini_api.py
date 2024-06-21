# google_gemini_api.py
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

def configure_gemini():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set.")
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

    response = model.generate_content([
        f"input: You are a Finance expert AI. Your task is to Provide data analysis, Summarize industry news and reports and Explain different investment strategies.\n\ncan you tell me about the stock {query}",
        "output: ",
    ])

    return response.text if response else None
