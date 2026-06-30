"""Main orchestration script for the PowerShell Behavioral Analytics Pipeline.

Run from the repository root:

    python -m src.main

The script will generate synthetic sample data if no input file is available.
"""

from __future__ import annotations

import logging

from .build_dataframe import build_analytics_dataframe
from .collect_logs import load_powershell_logs
from .config import (
    DEFAULT_INPUT_FILE,
    DEFAULT_PLOT_FILE,
    RESULTS_DIR,
    TOP_N_OUTLIERS,
)
from .detect_outliers import flag_top_residual_outliers
from .feature_engineering import engineer_behavioral_features
from .generate_sample_data import generate_sample_data
from .regression_model import add_regression_outputs, fit_behavioral_regression
from .report_generator import write_daily_summary, write_metrics, write_outlier_report
from .utils import configure_logging, ensure_directory
from .visualize_results import plot_regression_results

logger = logging.getLogger(__name__)


def run_pipeline() -> None:
    """Execute the end-to-end behavioral PowerShell analytics pipeline."""
    configure_logging()
    ensure_directory(RESULTS_DIR)

    if not DEFAULT_INPUT_FILE.exists():
        logger.info("Sample input file not found. Generating synthetic sample data.")
        generate_sample_data(DEFAULT_INPUT_FILE)

    raw_df = load_powershell_logs(DEFAULT_INPUT_FILE)
    analytics_df = build_analytics_dataframe(raw_df)
    feature_df = engineer_behavioral_features(analytics_df)

    model = fit_behavioral_regression(feature_df)
    scored_df = add_regression_outputs(feature_df, model)
    outlier_df = flag_top_residual_outliers(scored_df, TOP_N_OUTLIERS)

    plot_regression_results(outlier_df, DEFAULT_PLOT_FILE)
    write_outlier_report(outlier_df)
    write_daily_summary(outlier_df)
    write_metrics(model, outlier_df)

    logger.info("Pipeline complete. Outputs written to %s", RESULTS_DIR)


if __name__ == "__main__":
    run_pipeline()
