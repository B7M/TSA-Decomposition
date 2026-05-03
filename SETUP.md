# Setup and Reproduction Instructions

## Environment

- **Python:** 3.10+
- **Platform:** Notebooks were developed and executed on Google Colab (GPU runtime recommended but not required)
- **OS:** Any (Linux, macOS, Windows)

## Installation

### Option A: Google Colab (recommended)

1. Upload the notebook files to Google Colab
2. Upload the `data/processed/` folder to your Google Drive
3. Each notebook includes a Colab setup cell that mounts Drive and installs dependencies automatically
4. Select **Runtime → Change runtime type → GPU** for faster training (optional but recommended)

### Option B: Local environment

```bash
pip install -r requirements.txt
```

If running locally on an Apple Silicon Mac, MPS acceleration is not supported for Autoformer, the notebooks automatically fall back to CPU.

## Data

All datasets are included in `data/processed/`. No external downloads are required.

| File | Description | Source |
|------|-------------|--------|
| `BTC.csv` | Daily Bitcoin close price, Jan 2021 - Feb 2026 | CoinMarketCap |
| `SP500.csv` | Daily S&P 500 index level, Jan 2021 - Feb 2026 | FRED |
| `FRED_DGS10.csv` | Daily 10-year Treasury yield, Jan 2021 - Feb 2026 | FRED |

## Running the Notebooks

Each notebook is self-contained and runs top-to-bottom. The three notebooks share the same pipeline structure and can be run independently in any order.

```
notebooks/
├── Final_BTC.ipynb        # Bitcoin analysis
├── Final_SP500.ipynb      # S&P 500 analysis
└── Final_FRED.ipynb       # Treasury 10Y yield analysis
```

### Steps

1. Open any notebook
2. **Run All** (Kernel → Restart & Run All)
3. Outputs (figures, CSV tables, cached results) are saved to `results/figures_{DATASET}/`

### Execution time

| Notebook | GPU (Colab T4) | CPU |
|----------|---------------|-----|
| Final_BTC | ~30 min | ~2 hours |
| Final_SP500 | ~25 min | ~1.5 hours |
| Final_FRED | ~25 min | ~1.5 hours |

### Caching

The deep learning cross-validation results are cached to `.pkl` files after the first run, subsequent runs load from cache. **Delete the `.pkl` files if you change any model hyperparameters and need a fresh training run.**

Cache files are located at:
```
results/BTC/figures_BTC/BTC_dl_cv_multiseed.pkl
results/SP500/figures_SP500/SP500_dl_cv_multiseed.pkl
results/FRED/figures_FRED/FRED_dl_cv_multiseed.pkl
```

## Troubleshooting

**"ModuleNotFoundError: neuralforecast"** $\rightarrow$ Run `pip install neuralforecast` in the notebook or terminal.

**Training is very slow** $\rightarrow$ Switch to a GPU runtime on Colab (Runtime → Change runtime type → GPU).

**Results differ slightly from the report** $\rightarrow$ This can happen if a different PyTorch or NeuralForecast version is installed. The cached `.pkl` files contain the exact results used in the report.

**Lightning warnings clutter the output** $\rightarrow$ The notebooks include a logging suppression cell near the top. If warnings persist, they are cosmetic and do not affect results.
