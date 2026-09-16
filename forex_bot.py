import yfinance as yf
import pandas as pd

# Download EUR/USD hourly data
print("Downloading EUR/USD data...")

data = yf.download(
    "EURUSD=X",
    period="60d",
    interval="1h",
    auto_adjust=False
)

# Check whether we received data
if data.empty:
    print("No data was downloaded.")
else:
    print("Data downloaded successfully!")
    print(data.tail())
    print(f"\nNumber of candles: {len(data)}")