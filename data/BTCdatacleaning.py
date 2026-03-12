import pandas as pd

df = pd.read_csv("Bitcoin_1_1_2017-3_9_2026_historical_data_coinmarketcap.csv", sep=";")

out = pd.DataFrame({
    "Date": pd.to_datetime(df["timeOpen"]).dt.strftime("%-m/%-d/%Y"),
    "Open": df["open"],
    "High": df["high"],
    "Low": df["low"],
    "Close": df["close"],
    "Adj Close": df["close"], 
    "Volume": df["volume"].round().astype("Int64")
})

# Sort oldest to newest 
out["Date_dt"] = pd.to_datetime(out["Date"])
out = out.sort_values("Date_dt").drop(columns="Date_dt").reset_index(drop=True)

# Save result
out.to_csv("BTC_clean.csv", index=False)

print(out.head())
# print("\nSaved as: BTC_clean.csv")