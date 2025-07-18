# import yfinance as yf
# import pandas as pd

# symbol = "^NSEI"  # Nifty 50 symbol for yfinance
# df = yf.download(symbol, period="1d", interval="5m")
# df.to_csv("nifty50_5min_yfinance.csv")

import yfinance as yf
import pandas as pd
df = yf.download("ICICIBANK.NS", start="2025-07-17", end="2025-07-18", interval="5m")
df = df.reset_index()
df = df.set_index('Datetime')

# Convert UTC to IST (UTC+5:30)
df.index = df.index + pd.Timedelta(hours=5, minutes=30)
print(df)