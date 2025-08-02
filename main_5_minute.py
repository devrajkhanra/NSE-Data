# import yfinance as yf
# import pandas as pd

# symbol = "^NSEI"  # Nifty 50 symbol for yfinance
# df = yf.download(symbol, period="1d", interval="5m")
# df.to_csv("nifty50_5min_yfinance.csv")

import yfinance as yf
import pandas as pd

start = input('Enter start date (YYYY-MM-DD): ')
end = input('Enter end date (YYYY-MM-DD): ')

# Fetch 5-minute data
df = yf.download("^NSEI", start=start, end=end, interval="5m")

# Confirm data was received
if df is not None and not df.empty:
    df = df.reset_index()
    df = df.set_index('Datetime') if 'Datetime' in df.columns else df.set_index('Date')

    # Convert from UTC to IST
    df.index = df.index + pd.Timedelta(hours=5, minutes=30)

    print(df)
    df.to_csv(f"nifty50_5min_{start}.csv")
else:
    print("No data was retrieved. Check the ticker symbol or date range.")
