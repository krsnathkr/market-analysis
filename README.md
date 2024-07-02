# Market Radar

Welcome to Market Radar, a Streamlit-based application that provides detailed financial analyses and stock data visualizations using the Google Gemini API and Yahoo Finance.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Market Radar is designed to help investors and financial analysts gain insights into stock performance and make informed decisions. By leveraging the power of the Google Gemini API, this application generates comprehensive financial analyses, including key financials, major news, analyst ratings, and investment strategies. It also fetches and visualizes historical stock data using Yahoo Finance.

## Features
- Generate detailed financial analysis and insights for any stock ticker.
- Fetch and visualize historical stock price data.
- Interactive and user-friendly interface built with Streamlit.
- Securely handle API keys through Streamlit's sidebar input.

## Installation
To run Market Radar locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd market-analysis
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To start the application, run:
```bash
streamlit run app.py
```
This will open the application in your default web browser. You can then enter your Google Gemini API key and the stock ticker you want to analyze in the sidebar.

## Configuration
### API Key
To use the Google Gemini API, you need to obtain an API key from [Google AI Studio](https://aistudio.google.com/). Once you have the key, enter it in the sidebar of the application.

### Stock Ticker
Enter the stock ticker symbol (e.g., `AAPL` for Apple, `MU` for Micron Technology) in the sidebar to fetch and visualize the relevant financial data and analysis.

## Contributing
Contributions are welcome! If you have suggestions for improvements or want to report issues, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Developed by Krishna Thakar 💖