import os
import sys
import django

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock_prediction.settings')
django.setup()

from data_collection.models import StockPrice

import yfinance as yf
from django.utils import timezone

ticker = yf.Ticker("AAPL")
history = ticker.history(period="1d")
latest_data = history.iloc[-1]

stock_price = StockPrice(
    ticker="AAPL",
    date=timezone.now(),
    open=latest_data["Open"],
    high=latest_data["High"],
    low=latest_data["Low"],
    close=latest_data["Close"],
    volume=int(latest_data["Volume"]),
    market_cap=ticker.info.get("marketCap"),
    pe_ratio=ticker.info.get("trailingPE"),
    high_52_week=ticker.info.get("fiftyTwoWeekHigh"),
    low_52_week=ticker.info.get("fiftyTwoWeekLow"),
)

stock_price.save()
