"""Outlier detection module.

Outliers are selected based on absolute residual distance from the regression line.
This reflects the original analytical insight: normal PowerShell scripts cluster
near the expected length/whitespace relationship, while suspicious scripts deviate.
"""

from __future__ import annotations

import logging

import pandas as pd

from .config import ABS_RESIDUAL_COLUMN, OUTLIER_COLUMN, RESIDUAL_COLUMN, TOP_N_OUTLIERS

logger = logging.getLogger(__name__)


def flag_top_residual_outliers(df: pd.DataFrame, top_n: int = TOP_N_OUTLIERS) -> pd.DataFrame:
    """Flag the top N scripts with the largest absolute residuals."""
    logger.info("Flagging top %s residual outliers", top_n)

    outlier_df = df.copy()
    outlier_df[ABS_RESIDUAL_COLUMN] = outlier_df[RESIDUAL_COLUMN].abs()
    outlier_df[OUTLIER_COLUMN] = False

    if len(outlier_df) == 0:
        return outlier_df

    top_indices = outlier_df.nlargest(top_n, ABS_RESIDUAL_COLUMN).index
    outlier_df.loc[top_indices, OUTLIER_COLUMN] = True

    logger.info("Flagged %s outlier candidates", len(top_indices))
    return outlier_df


def get_outliers(df: pd.DataFrame) -> pd.DataFrame:
    """Return records flagged as behavioral outliers."""
    return df[df[OUTLIER_COLUMN]].copy().sort_values(ABS_RESIDUAL_COLUMN, ascending=False)
