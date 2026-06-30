"""Visualization module for regression and outlier results."""

from __future__ import annotations

import logging
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from .config import (
    OUTLIER_COLUMN,
    PREDICTED_WHITESPACE_COLUMN,
    SCRIPT_LENGTH_COLUMN,
    WHITESPACE_COUNT_COLUMN,
)

logger = logging.getLogger(__name__)


def plot_regression_results(df: pd.DataFrame, output_file: Path) -> None:
    """Create a scatter plot with regression line and highlighted outliers."""
    logger.info("Creating regression plot at %s", output_file)

    output_file.parent.mkdir(parents=True, exist_ok=True)

    sorted_df = df.sort_values(SCRIPT_LENGTH_COLUMN)

    plt.figure(figsize=(10, 6))
    normal_df = df[~df[OUTLIER_COLUMN]]
    outlier_df = df[df[OUTLIER_COLUMN]]

    plt.scatter(
        normal_df[SCRIPT_LENGTH_COLUMN],
        normal_df[WHITESPACE_COUNT_COLUMN],
        alpha=0.45,
        label="Normal PowerShell activity",
    )

    plt.scatter(
        outlier_df[SCRIPT_LENGTH_COLUMN],
        outlier_df[WHITESPACE_COUNT_COLUMN],
        marker="x",
        s=90,
        label="Outlier candidates",
    )

    plt.plot(
        sorted_df[SCRIPT_LENGTH_COLUMN],
        sorted_df[PREDICTED_WHITESPACE_COLUMN],
        label="Expected behavior regression line",
    )

    plt.title("PowerShell Behavioral Anomaly Detection")
    plt.xlabel("Script Length")
    plt.ylabel("Whitespace Count")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_file, dpi=150)
    plt.close()

    logger.info("Regression plot saved")
