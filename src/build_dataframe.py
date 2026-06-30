"""DataFrame preparation module."""

from __future__ import annotations

import logging

import pandas as pd

from .config import HOST_COLUMN, SCRIPT_COLUMN, TIMESTAMP_COLUMN

logger = logging.getLogger(__name__)


def build_analytics_dataframe(raw_df: pd.DataFrame) -> pd.DataFrame:
    """Prepare raw PowerShell logs for feature engineering.

    The function standardizes timestamps, removes records with empty script text,
    and keeps only the fields required for the public analytical workflow.
    """
    logger.info("Preparing analytics DataFrame")

    df = raw_df[[TIMESTAMP_COLUMN, HOST_COLUMN, SCRIPT_COLUMN]].copy()
    df[TIMESTAMP_COLUMN] = pd.to_datetime(df[TIMESTAMP_COLUMN], errors="coerce")
    df = df.dropna(subset=[TIMESTAMP_COLUMN, SCRIPT_COLUMN])
    df[SCRIPT_COLUMN] = df[SCRIPT_COLUMN].astype(str)

    logger.info("Prepared analytics DataFrame with %s records", len(df))
    return df
