# When Does Time-Series Decomposition Help or Hurt Long-Horizon Forecasting?

---

## Overview

This project investigates whether explicit time-series decomposition improves or degrades long-horizon forecasting on financial data. We compare an Autoformer model (with a built-in moving-average decomposition block) against an ablated variant without decomposition and a Temporal Convolutional Network (TCN) that learns directly from raw data. Classical ARIMA and SARIMA models serve as statistical baselines. The analysis spans three datasets, Bitcoin (BTC), the S&P 500, and the 10-year U.S. Treasury yield, chosen for their distinct structural properties.

---

## Repository Structure

```
├── data/
│   └── processed/              # Cleaned daily series (BTC, SP500, FRED DGS10)
├── notebooks/
│   ├── Final_BTC.ipynb         # Full analysis notebook for Bitcoin
│   ├── Final_SP500.ipynb       # Full analysis notebook for S&P 500
│   └── Final_FRED.ipynb        # Full analysis notebook for Treasury 10Y yield
├── results/
│   ├── BTC/                    # BTC outputs (plots, CSVs, cached CV results)
│   ├── SP500/                  # SP500 outputs
│   └── FRED/                   # FRED outputs
├── requirements.txt            # Python dependencies
├── SETUP.md                    # Reproduction instructions
└── README.md
```

---

## Data Sources

All data spans January 2021 through early 2026.

| Dataset | Source | Frequency | Series |
|---------|--------|-----------|--------|
| Bitcoin | [CoinMarketCap](https://coinmarketcap.com/currencies/bitcoin/historical-data/) | Daily | Close price (USD) |
| S&P 500 | [FRED](https://fred.stlouisfed.org) | Daily | SP500 index level |
| Treasury yields | [FRED](https://fred.stlouisfed.org) | Daily | DGS10 (10-year constant maturity, %) |

The Treasury yield curve data used for PCA analysis includes all maturities from 1-month to 30-year:
DGS1MO, DGS3MO, DGS6MO, DGS1, DGS2, DGS3, DGS5, DGS7, DGS10, DGS20, DGS30.

Data provider: Board of Governors of the Federal Reserve System (US), H.15 Selected Interest Rates release.

---

## Methods

- **Classical baselines:** ARIMA and SARIMA with AICc-based order selection
- **Deep learning models:** TCN (dilations [1,2,4,8], kernel size 3), Autoformer (with decomposition), Autoformer NoDecomp (decomposition disabled via window=1)
- **Evaluation:** Rolling-origin cross-validation across 3 seeds, forecast horizons $h = 7, 14, 30$ days
- **Statistical testing:** Diebold-Mariano tests with HLN correction, volatility-regime conditional analysis, log-returns robustness check
- **Ablation studies:** TCN kernel size sweep, Autoformer moving-average window sweep

---

## Reproducing Results

Each notebook runs end-to-end. The deep learning CV results are cached to `.pkl` files after the first run; subsequent runs load from cache unless the file is deleted.

```bash
# Install dependencies
pip install neuralforecast statsmodels dill seaborn scikit-learn

# Run any notebook
jupyter notebook Final_BTC.ipynb
```

**Note:** Deep learning training was performed on Google Colab. On CPU, a full notebook run takes approximately 2–3 hours per dataset. Delete the `.pkl` cache files if you change any model hyperparameters.

---

## License and Data Usage

Data usage is subject to [FRED terms of use](https://fred.stlouisfed.org/legal). This repository is for academic purposes.
