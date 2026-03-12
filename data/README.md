# Financial Time Series Datasets

This repository contains multiple **financial time-series datasets** used for statistical modeling, forecasting, and volatility analysis.  
The datasets span **macroeconomic interest rates, equity markets, and cryptocurrency markets**, enabling comparative analysis across different financial domains.

These datasets are intended for experiments in:

- Time-series forecasting (ARIMA, SARIMA, deep learning models)
- Volatility modeling (ARCH/GARCH)
- Financial return analysis
- Cross-market comparisons
- Machine learning applied to financial data

The goal of this repository is to provide **clean, structured datasets suitable for reproducible time-series modeling experiments.**

---

# Datasets Included

1. **U.S. Treasury Yield Curve (FRED)**
2. **S&P 500 Index**
3. **Bitcoin Historical Market Data**

These datasets represent three major financial domains:

| Dataset | Domain | Asset Type | Frequency |
|-------|-------|-----------|-----------|
| Treasury Yield Curve | Macroeconomics | Interest Rates | Daily |
| S&P 500 | Equity Markets | Stock Index | Daily |
| Bitcoin | Cryptocurrency | Digital Asset | Daily |

Together they allow comparative modeling across:

- macroeconomic indicators
- equity market behavior
- cryptocurrency market dynamics

---

# 1. U.S. Treasury Yield Curve Data (FRED)

**Source:** Federal Reserve Economic Data (FRED)  
**Provider:** Federal Reserve Bank of St. Louis  
**Release:** H.15 Selected Interest Rates  
**Frequency:** Daily  
**Units:** Percent  
**Seasonal Adjustment:** Not seasonally adjusted  

This dataset contains **daily constant-maturity Treasury yields** for multiple maturities ranging from **1 month to 30 years**.

The yields are derived from actively traded Treasury securities and interpolated to produce **constant maturity estimates along the yield curve**.

The yield curve is widely used in:

- macroeconomic research
- interest-rate forecasting
- yield curve modeling
- financial risk analysis
- term structure estimation

### Treasury Yield Series

| Column | Description |
|------|-------------|
| observation_date | Date of observation |
| DGS1MO | 1-Month Treasury yield |
| DGS3MO | 3-Month Treasury yield |
| DGS6MO | 6-Month Treasury yield |
| DGS1 | 1-Year Treasury yield |
| DGS2 | 2-Year Treasury yield |
| DGS3 | 3-Year Treasury yield |
| DGS5 | 5-Year Treasury yield |
| DGS7 | 7-Year Treasury yield |
| DGS10 | 10-Year Treasury yield |
| DGS20 | 20-Year Treasury yield |
| DGS30 | 30-Year Treasury yield |

### Example CSV Structure

```csv
observation_date,DGS1MO,DGS3MO,DGS6MO,DGS1,DGS2,DGS3,DGS5,DGS7,DGS10,DGS20,DGS30
2000-01-03,5.27,5.45,5.67,5.89,6.03,6.15,6.28,6.35,6.45,6.47,6.48
2000-01-04,5.30,5.48,5.70,5.92,6.05,6.17,6.30,6.37,6.47,6.49,6.50
```

### Methodology

Treasury yields follow the **Treasury Yield Curve Methodology**, which estimates constant maturity yields from outstanding Treasury securities.

More information:

https://www.federalreserve.gov/releases/h15/  
https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics/treasury-yield-curve-methodology

---

# 2. S&P 500 Index Data

**Source:** S&P Dow Jones Indices LLC  
**Accessed via:** FRED (Federal Reserve Bank of St. Louis)  
**Series ID:** SP500  
**Frequency:** Daily  
**Units:** Index value  
**Seasonal Adjustment:** Not seasonally adjusted  

The **S&P 500 Index** tracks the performance of **500 large-cap U.S. companies** and is one of the most widely used benchmarks for the U.S. equity market.

It represents approximately **75% of total U.S. equity market capitalization**.

Typical applications include:

- equity return analysis
- market volatility modeling
- portfolio benchmarking
- macro-financial research

### Dataset Columns

| Column | Description |
|------|-------------|
| observation_date | Trading date |
| SP500 | Daily closing value of the S&P 500 index |

### Example CSV Structure

```csv
observation_date,SP500
2000-01-03,1455.22
2000-01-04,1399.42
2000-01-05,1402.11
```

Suggested citation:

S&P Dow Jones Indices LLC  
*S&P 500 [SP500]* retrieved from Federal Reserve Bank of St. Louis FRED database  
https://fred.stlouisfed.org/series/SP500

---

# 3. Bitcoin Historical Market Data

**Source:** CoinMarketCap  
**Frequency:** Daily  
**Units:** USD price and trading volume  
**Seasonal Adjustment:** Not seasonally adjusted  

This dataset contains **daily historical market data for Bitcoin**, including price and trading volume aggregated across major cryptocurrency exchanges.

Bitcoin is a **decentralized digital asset introduced in 2009 by Satoshi Nakamoto** and is widely studied in cryptocurrency research.

Unlike traditional markets, cryptocurrency markets operate **24 hours per day, 7 days per week**, producing distinct volatility dynamics.

### Bitcoin Dataset Columns

| Column | Description |
|------|-------------|
| Date | Trading date |
| Open | Opening price |
| High | Highest price during the day |
| Low | Lowest price during the day |
| Close | Closing price |
| Adj Close | Adjusted closing price |
| Volume | Total trading volume |

### Example CSV Structure

```csv
Date,Open,High,Low,Close,Adj Close,Volume
2017-01-01,998.33,1005.00,960.00,995.44,995.44,40570900
2017-01-02,995.44,1031.39,991.50,1017.32,1017.32,66038000
```

### Notes

Cryptocurrency markets differ from traditional financial markets in several ways:

- continuous **24/7 trading**
- higher volatility
- liquidity fragmentation across exchanges

These characteristics make Bitcoin particularly useful for studying:

- volatility clustering
- heavy-tailed return distributions
- market regime changes

Methodology details:

https://coinmarketcap.com/methodology/

---

# Potential Applications

These datasets support a wide range of **financial time-series modeling tasks**:

### Statistical Models

- ARIMA / ARMA forecasting
- Seasonal ARIMA models
- structural time-series models

### Volatility Models

- ARCH / GARCH models
- volatility clustering analysis
- risk modeling

### Machine Learning

- deep learning forecasting
- convolutional time-series models
- transformer-based forecasting architectures

### Financial Research

- cross-market comparisons
- macro-financial relationships
- market regime analysis

---

# Data Licensing and Terms

Please refer to the original data providers for licensing and usage policies.

FRED Terms of Use  
https://fred.stlouisfed.org/legal#fred-terms-faq  

S&P Dow Jones Indices licensing  
https://www.spglobal.com/spdji/  

CoinMarketCap methodology and usage policies  
https://coinmarketcap.com/methodology/

---

# References

Federal Reserve Bank of St. Louis  
FRED Economic Data  
https://fred.stlouisfed.org  

S&P Dow Jones Indices LLC  
S&P 500 Index  
https://fred.stlouisfed.org/series/SP500  

CoinMarketCap  
Bitcoin Historical Data  
https://coinmarketcap.com/currencies/bitcoin/historical-data/