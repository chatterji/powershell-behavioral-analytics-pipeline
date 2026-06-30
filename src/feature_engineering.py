"""Behavioral feature engineering for PowerShell threat detection.

The original solution was based on two Red Team-informed behavioral indicators:

1. Malicious PowerShell scripts were often longer than normal administrative scripts.
2. Malicious scripts often contained fewer blank spaces because of compression,
   obfuscation, or dense payload construction.

This module turns raw script text into those explainable analytical features.
"""

from __future__ import annotations

import logging

import pandas as pd

from .config import SCRIPT_COLUMN, SCRIPT_LENGTH_COLUMN, WHITESPACE_COUNT_COLUMN

logger = logging.getLogger(__name__)


def calculate_script_length(script_text: str) -> int:
    """Return the total character length of a PowerShell script."""
    return len(str(script_text))


def calculate_whitespace_count(script_text: str) -> int:
    """Return the number of blank spaces in a PowerShell script.

    The original notebook focused on blank spaces specifically, not all whitespace.
    This keeps the feature aligned with the original implementation.
    """
    return str(script_text).count(" ")


def engineer_behavioral_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add script length and whitespace count features to a DataFrame."""
    logger.info("Engineering behavioral PowerShell features")

    feature_df = df.copy()
    feature_df[SCRIPT_LENGTH_COLUMN] = feature_df[SCRIPT_COLUMN].apply(calculate_script_length)
    feature_df[WHITESPACE_COUNT_COLUMN] = feature_df[SCRIPT_COLUMN].apply(calculate_whitespace_count)

    logger.info("Feature engineering complete")
    return feature_df
