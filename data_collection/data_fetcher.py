import os
import sys
import django

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock_prediction.settings')
django.setup()

from data_collection.models import StockPrice
import yfinance as yf
from django.utils import timezone

# Delete all records in the StockPrice model
StockPrice.objects.all().delete()
print("All existing stock data deleted.")


tickers = ["NVDA", "GSAT", "INTC", "SMCI", "AMZN", "DJT", "AAPL", "TSLA", "PTON", "NIO", "SOFI", "SNAP", "F", "LCID", "AMD", "BBD", "NU", "PFE", "MARA", "GOOGL", "T", "PLTR", "UBER", "AES", "RIG", "WBD", "MSTR", "CMCSA", "MSFT", "BAC", "CLSK", "AGNC", "ITUB", "RIOT", "AAL", "UMC", "GOOG", "HOOD", "WULF", "XOM", "VALE", "MRVL", "RIVN", "OKLO", "CSCO", "ABEV", "LUMN", "CCL", "AVGO", "BA", "MBLY", "BTE", "JBLU", "PBR", "IQ", "GOLD", "W", "PYPL", "CMG", "AMCR", "KVUE", "META", "IONQ", "COIN", "ERIC", "AUR", "MU", "CVS", "LYFT", "KGC", "VZ", "WFC", "BTG", "ET", "GRAB", "KDP", "BMY", "ALTM", "HPE", "HIMS", "WBA", "HL", "TSM", "DELL", "NEE", "ADMA", "HBAN", "C", "CVX", "RBLX", "JOBY", "VRN", "RDDT", "NCLH", "KMI", "CSX", "RKLB", "NOK", "PRMW"]

for stock in tickers:
    ticker = yf.Ticker(stock)
    history = ticker.history(period="1d")

    if not history.empty:
        latest_data = history.iloc[-1]
        stock_date = timezone.now().date()

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
            print(f"Stock price for {stock} added successfully!")
        else:
            print(f"Stock price for {stock} already exists for the current date!")
    else:
        print(f"No data found for {stock}!")
