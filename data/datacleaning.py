import pandas as pd
import os

FRED_PATH = "./data/raw/FRED.csv"
SP500_PATH = "./data/raw/SP500.csv"
BTC_PATH = "./data/raw/Bitcoin_historical_data_coinmarketcap.csv"

os.makedirs("cleaned_data", exist_ok=True)

# =========================
# S&P500 (clean first to get start date)
# =========================
sp500 = pd.read_csv(SP500_PATH)

sp500 = sp500[["observation_date","SP500"]]

sp500 = sp500.rename(columns={
    "observation_date":"date",
    "SP500":"sp500"
})

sp500["date"] = pd.to_datetime(sp500["date"])
sp500["sp500"] = pd.to_numeric(sp500["sp500"], errors="coerce")

sp500 = sp500.sort_values("date")
sp500 = sp500.drop_duplicates("date")
sp500 = sp500.dropna()

# determine start of S&P dataset (10-year window)
start_date = sp500["date"].min()

sp500.to_csv("cleaned_data/sp500_cleaned.csv", index=False)

print("SP500 cleaned:", sp500.shape)
print("SP500 start date:", start_date.date())


# =========================
# Treasury (DGS10 only)
# =========================
fred = pd.read_csv(FRED_PATH)

fred = fred[["observation_date","DGS10"]]

fred = fred.rename(columns={
    "observation_date":"date",
    "DGS10":"dgs10"
})

fred["date"] = pd.to_datetime(fred["date"])
fred["dgs10"] = pd.to_numeric(fred["dgs10"], errors="coerce")

fred = fred.sort_values("date")
fred = fred.drop_duplicates("date")
fred = fred.dropna()

# keep only same time window as S&P
fred = fred[fred["date"] >= start_date]

fred.to_csv("cleaned_data/treasury_dgs10.csv", index=False)

print("Treasury cleaned:", fred.shape)


# =========================
# Bitcoin
# =========================
btc = pd.read_csv(BTC_PATH, sep=";")

btc.columns = [c.strip().replace('"','') for c in btc.columns]

btc = btc[["timeOpen","close"]]

btc["date"] = pd.to_datetime(btc["timeOpen"], utc=True)
btc["date"] = btc["date"].dt.tz_convert(None).dt.normalize()

btc = btc.rename(columns={
    "close":"btc_close"
})

btc = btc[["date","btc_close"]]

btc["btc_close"] = pd.to_numeric(btc["btc_close"], errors="coerce")
btc = btc[btc["date"] >= start_date]
btc = btc.sort_values("date")
btc = btc.drop_duplicates("date")
btc = btc.dropna()

# keep only same time window as S&P
btc = btc[btc["date"] >= start_date]

btc.to_csv("cleaned_data/bitcoin_close.csv", index=False)

print("Bitcoin cleaned:", btc.shape)