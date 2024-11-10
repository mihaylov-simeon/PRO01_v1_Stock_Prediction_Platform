import os
import sys
import django

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock_prediction.settings')
django.setup()

from data_collection.models import StockPrice, HistoricalPrice
import yfinance as yf
from django.utils import timezone

tickers = ["NVDA", "GSAT", "INTC", "SMCI", "AMZN", "DJT", "AAPL", "TSLA", "PTON", "NIO", "SOFI", "SNAP", "F", "LCID", "AMD", "BBD", "NU", "PFE", "MARA", "GOOGL", "T", "PLTR", "UBER", "AES", "RIG", "WBD", "MSTR", "CMCSA", "MSFT", "BAC", "CLSK", "AGNC", "ITUB", "RIOT", "AAL", "UMC", "GOOG", "HOOD", "WULF", "XOM", "VALE", "MRVL", "RIVN", "OKLO", "CSCO", "ABEV", "LUMN", "CCL", "AVGO", "BA", "MBLY", "BTE", "JBLU", "PBR", "IQ", "GOLD", "W", "PYPL", "CMG", "AMCR", "KVUE", "META", "IONQ", "COIN", "ERIC", "AUR", "MU", "CVS", "LYFT", "KGC", "VZ", "WFC", "BTG", "ET", "GRAB", "KDP", "BMY", "ALTM", "HPE", "HIMS", "WBA", "HL", "TSM", "DELL", "NEE", "ADMA", "HBAN", "C", "CVX", "RBLX", "JOBY", "VRN", "RDDT", "NCLH", "KMI", "CSX", "RKLB", "NOK", "PRMW"]

# Move existing StockPrice data to HistoricalPrice
for existing_stock in StockPrice.objects.all():
    # Add the existing StockPrice data to HistoricalPrice if not already there
    if not HistoricalPrice.objects.filter(ticker=existing_stock.ticker, date=existing_stock.date).exists():
        HistoricalPrice.objects.create(
            ticker=existing_stock.ticker,
            date=existing_stock.date,
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
    # Delete the entry from StockPrice after transferring
    existing_stock.delete()

print("Moved existing StockPrice data to HistoricalPrice and cleared StockPrice table for today's data.")

# Fetch today's data and update StockPrice
for stock in tickers:
    ticker = yf.Ticker(stock)
    history = ticker.history(period="1d")

    if not history.empty:
        latest_data = history.iloc[-1]
        stock_date = timezone.now().date()

        # Save today's data to StockPrice
        if not StockPrice.objects.filter(ticker=stock, date__date=stock_date).exists():
            stock_price = StockPrice(
                ticker=stock,
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
            print(f"Today's stock price for {stock} added to StockPrice!")

        # Ensure HistoricalPrice does not have today's data
        if HistoricalPrice.objects.filter(ticker=stock, date=stock_date).exists():
            HistoricalPrice.objects.filter(ticker=stock, date=stock_date).delete()

    else:
        print(f"No data found for {stock}!")

