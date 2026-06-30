# Feature Engineering

## Engineered Features

### Script Length

Measures the total number of characters in each script.

### Whitespace Count

Measures the total number of blank spaces.

These features form a two-dimensional behavioral representation of every
PowerShell script.

## Why It Worked

Legitimate administrative scripts generally followed a predictable
relationship between length and whitespace. Malicious scripts frequently
deviated from this pattern, allowing them to be isolated through
residual analysis.
