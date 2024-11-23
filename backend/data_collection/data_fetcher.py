import os
import sys

# Add the project directory to PYTHONPATH
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_dir)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock_prediction.settings')
import django
django.setup()

from data_collection.models import StockPrice, HistoricalPrice
import yfinance as yf
from django.utils.timezone import is_naive, make_aware, now

tickers = [
    "NVDA", "GSAT", "INTC", "SMCI", "AMZN", "DJT", "AAPL", "TSLA", "PTON", "NIO",
    "SOFI", "SNAP", "F", "LCID", "AMD", "BBD", "NU", "PFE", "MARA", "GOOGL",
    "T", "PLTR", "UBER", "AES", "RIG", "WBD", "MSTR", "CMCSA", "MSFT", "BAC",
    # Add more tickers if needed...
]

# Move existing StockPrice data to HistoricalPrice
for existing_stock in StockPrice.objects.all():
    if not HistoricalPrice.objects.filter(ticker=existing_stock.ticker, date=existing_stock.date).exists():
        date_to_save = existing_stock.date
        if is_naive(date_to_save):
            date_to_save = make_aware(date_to_save)

        HistoricalPrice.objects.create(
            ticker=existing_stock.ticker,
            date=date_to_save,
            open=existing_stock.open,
            high=existing_stock.high,
            low=existing_stock.low,
            close=existing_stock.close,
            volume=existing_stock.volume,
            market_cap=existing_stock.market_cap,
            pe_ratio=existing_stock.pe_ratio,
            high_52_week=existing_stock.high_52_week,
            low_52_week=existing_stock.low_52_week,
        )
    existing_stock.delete()

print("Moved existing StockPrice data to HistoricalPrice and cleared StockPrice table.")

# Fetch today's data and update StockPrice
for stock in tickers:
    ticker = yf.Ticker(stock)
    history = ticker.history(period="1d")

    if not history.empty:
        latest_data = history.iloc[-1]
        stock_date = now().date()

        if not StockPrice.objects.filter(ticker=stock, date__date=stock_date).exists():
            stock_price = StockPrice(
                ticker=stock,
                date=now(),
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
            print(f"Added stock price for {stock}!")
    else:
        print(f"No data found for {stock}.")