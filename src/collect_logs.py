"""Log collection module.

In the original enterprise implementation, prior-day PowerShell logs were collected
and loaded into Hadoop for analysis. This public version reads synthetic data from
a CSV file while preserving the same pipeline boundary.
"""

from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd

from .config import HOST_COLUMN, SCRIPT_COLUMN, TIMESTAMP_COLUMN
from .utils import validate_columns

logger = logging.getLogger(__name__)


def load_powershell_logs(input_file: Path) -> pd.DataFrame:
    """Load PowerShell logs from a CSV file.

    Parameters
    ----------
    input_file:
        Path to a CSV containing timestamp, hostname, and script_text columns.

    Returns
    -------
    pandas.DataFrame
        Raw PowerShell log data.
    """
    logger.info("Loading PowerShell logs from %s", input_file)

    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    df = pd.read_csv(input_file)
    validate_columns(df, [TIMESTAMP_COLUMN, HOST_COLUMN, SCRIPT_COLUMN])

    logger.info("Loaded %s PowerShell log records", len(df))
    return df
