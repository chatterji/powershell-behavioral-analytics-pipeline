"""Utility helpers for logging, directories, and validation."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Iterable

import pandas as pd


def configure_logging(level: int = logging.INFO) -> None:
    """Configure consistent console logging for pipeline execution."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )


def ensure_directory(path: Path) -> None:
    """Create a directory if it does not already exist."""
    path.mkdir(parents=True, exist_ok=True)


def validate_columns(df: pd.DataFrame, required_columns: Iterable[str]) -> None:
    """Raise a clear error if required columns are missing."""
    missing = [column for column in required_columns if column not in df.columns]
    if missing:
        raise ValueError(f"Input data is missing required columns: {missing}")
