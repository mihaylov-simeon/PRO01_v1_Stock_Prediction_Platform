import os
import sys
import django

# Set the project directory in the PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock_prediction.settings')
django.setup()

from data_collection.models import StockPrice

import yfinance as yf
from django.utils import timezone

# Fetch stock data using yfinance
ticker = yf.Ticker("AAPL")  # Corrected the ticker symbol (it's "AAPL" not "APPL")
history = ticker.history(period="1d")
latest_data = history.iloc[-1]

# Create a new StockPrice instance with the latest data
stock_price = StockPrice(
    ticker="AAPL",  # `ticker` should be a string, not the Ticker object
    date=timezone.now(),
    open=latest_data["Open"],  # Use square brackets to access column values
    high=latest_data["High"],
    low=latest_data["Low"],
    close=latest_data["Close"],
    volume=int(latest_data["Volume"]),  # Ensure volume is an integer
    market_cap=ticker.info.get("marketCap"),  # Access info fields with .get() to avoid KeyError
    pe_ratio=ticker.info.get("trailingPE"),  # Update this field name to match yfinance's naming convention
    high_52_week=ticker.info.get("fiftyTwoWeekHigh"),
    low_52_week=ticker.info.get("fiftyTwoWeekLow"),
)

# Save to the database
stock_price.save()
