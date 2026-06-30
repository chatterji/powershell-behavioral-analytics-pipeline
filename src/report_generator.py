"""Report generation module for daily analytics outputs."""

from __future__ import annotations

import json
import logging
from pathlib import Path

import pandas as pd

from .config import (
    ABS_RESIDUAL_COLUMN,
    DEFAULT_DAILY_OUTPUT_FILE,
    DEFAULT_METRICS_FILE,
    DEFAULT_OUTLIER_FILE,
    HOST_COLUMN,
    OUTLIER_COLUMN,
    RESIDUAL_COLUMN,
    SCRIPT_LENGTH_COLUMN,
    TIMESTAMP_COLUMN,
    WHITESPACE_COUNT_COLUMN,
)

logger = logging.getLogger(__name__)


def write_outlier_report(df: pd.DataFrame, output_file: Path = DEFAULT_OUTLIER_FILE) -> None:
    """Write the outlier candidate report to CSV."""
    output_file.parent.mkdir(parents=True, exist_ok=True)

    columns = [
        TIMESTAMP_COLUMN,
        HOST_COLUMN,
        SCRIPT_LENGTH_COLUMN,
        WHITESPACE_COUNT_COLUMN,
        RESIDUAL_COLUMN,
        ABS_RESIDUAL_COLUMN,
        OUTLIER_COLUMN,
    ]
    df[df[OUTLIER_COLUMN]][columns].to_csv(output_file, index=False)
    logger.info("Outlier report written to %s", output_file)


def write_daily_summary(df: pd.DataFrame, output_file: Path = DEFAULT_DAILY_OUTPUT_FILE) -> None:
    """Write a one-row daily summary file."""
    output_file.parent.mkdir(parents=True, exist_ok=True)

    summary = {
        "total_scripts": len(df),
        "outliers_found": int(df[OUTLIER_COLUMN].sum()),
        "average_script_length": float(df[SCRIPT_LENGTH_COLUMN].mean()),
        "average_whitespace_count": float(df[WHITESPACE_COUNT_COLUMN].mean()),
        "max_absolute_residual": float(df[ABS_RESIDUAL_COLUMN].max()),
    }
    pd.DataFrame([summary]).to_csv(output_file, index=False)
    logger.info("Daily summary written to %s", output_file)


def write_metrics(model, df: pd.DataFrame, output_file: Path = DEFAULT_METRICS_FILE) -> None:
    """Write model and pipeline metrics to JSON."""
    output_file.parent.mkdir(parents=True, exist_ok=True)

    metrics = {
        "model_type": "LinearRegression",
        "intercept": float(model.intercept_),
        "coefficient_script_length": float(model.coef_[0]),
        "total_scripts": int(len(df)),
        "outliers_found": int(df[OUTLIER_COLUMN].sum()),
    }
    output_file.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    logger.info("Metrics written to %s", output_file)
