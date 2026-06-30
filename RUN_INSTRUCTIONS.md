# Phase 2 Run Instructions

## Install dependencies

```bash
pip install -r requirements.txt
```

## Generate synthetic sample data

```bash
python -m src.generate_sample_data
```

## Run the full pipeline

```bash
python -m src.main
```

## Run tests

```bash
pytest
```

## Expected outputs

The pipeline writes files to `results/`:

- `daily_summary.csv`
- `outliers.csv`
- `analytics_metrics.json`
- `sample_regression_plot.png`
