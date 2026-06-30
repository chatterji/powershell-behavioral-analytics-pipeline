"""Central configuration for the PowerShell Behavioral Analytics Pipeline.

The original enterprise implementation processed prior-day PowerShell logs in a
Hadoop environment. This public portfolio version uses local CSV files and
synthetic data to demonstrate the same analytical workflow without exposing
confidential production logs.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data"
RESULTS_DIR = PROJECT_ROOT / "results"

DEFAULT_INPUT_FILE = DATA_DIR / "sample_powershell_logs.csv"
DEFAULT_DAILY_OUTPUT_FILE = RESULTS_DIR / "daily_summary.csv"
DEFAULT_OUTLIER_FILE = RESULTS_DIR / "outliers.csv"
DEFAULT_METRICS_FILE = RESULTS_DIR / "analytics_metrics.json"
DEFAULT_PLOT_FILE = RESULTS_DIR / "sample_regression_plot.png"

# Expected input columns. Public sample data uses synthetic values only.
TIMESTAMP_COLUMN = "timestamp"
HOST_COLUMN = "hostname"
SCRIPT_COLUMN = "script_text"

# Engineered feature columns.
SCRIPT_LENGTH_COLUMN = "script_length"
WHITESPACE_COUNT_COLUMN = "whitespace_count"
PREDICTED_WHITESPACE_COLUMN = "predicted_whitespace_count"
RESIDUAL_COLUMN = "residual"
ABS_RESIDUAL_COLUMN = "absolute_residual"
OUTLIER_COLUMN = "is_outlier"

# Model settings.
TOP_N_OUTLIERS = 2
RANDOM_SEED = 42

# Synthetic data defaults.
DEFAULT_SAMPLE_SIZE = 1000
DEFAULT_OUTLIER_COUNT = 2
