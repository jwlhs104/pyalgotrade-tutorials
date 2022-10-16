import yfinance
import pandas as pd
from rest import FtxClient
from datetime import datetime

def format_Date_Time(row):
    return row['Date Time'].replace('T', ' ').split('+')[0]

client = FtxClient()
data = client.get_historical_prices(
    market='ETH-PERP',
    resolution=3600,
    start_time=datetime(2017, 5, 1).timestamp()
    )
# data = yfinance.download("SPY", start="1999-05-01", end="2022-10-16")
# data.to_csv("spy.csv")

df = pd.DataFrame(data)
df.drop(columns=['time'], inplace=True)
df = df.rename(columns={
    "startTime": "Date Time",
    "open": "Open",
    "high": "High",
    "close": "Close",
    "low": "Low",
    "volume": "Volume",
    })
df['Adj Close'] = df['Close']
df['Date Time'] = df.apply(lambda row: format_Date_Time(row), axis=1)
df.to_csv("eth.csv", index=False)
# print(df)

# time = df.apply(lambda row: format_Time(row), axis=1)
# print(time)
