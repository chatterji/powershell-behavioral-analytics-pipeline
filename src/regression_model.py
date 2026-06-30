"""Regression modeling module for behavioral anomaly detection.

Linear regression is used here as an explainable baseline for expected PowerShell
script behavior. The model estimates the expected relationship between script
length and whitespace count. Scripts with large residuals are flagged for review.
"""

from __future__ import annotations

import logging

import pandas as pd
from sklearn.linear_model import LinearRegression

from .config import (
    PREDICTED_WHITESPACE_COLUMN,
    RESIDUAL_COLUMN,
    SCRIPT_LENGTH_COLUMN,
    WHITESPACE_COUNT_COLUMN,
)

logger = logging.getLogger(__name__)


def fit_behavioral_regression(df: pd.DataFrame) -> LinearRegression:
    """Fit linear regression using script length to estimate whitespace count."""
    logger.info("Fitting behavioral regression model")

    x = df[[SCRIPT_LENGTH_COLUMN]]
    y = df[WHITESPACE_COUNT_COLUMN]

    model = LinearRegression()
    model.fit(x, y)

    logger.info(
        "Regression model fitted: intercept=%.4f, coefficient=%.4f",
        model.intercept_,
        model.coef_[0],
    )
    return model


def add_regression_outputs(df: pd.DataFrame, model: LinearRegression) -> pd.DataFrame:
    """Add predicted whitespace and residual columns to the DataFrame."""
    scored_df = df.copy()

    predictions = model.predict(scored_df[[SCRIPT_LENGTH_COLUMN]])
    scored_df[PREDICTED_WHITESPACE_COLUMN] = predictions
    scored_df[RESIDUAL_COLUMN] = scored_df[WHITESPACE_COUNT_COLUMN] - predictions

    return scored_df
