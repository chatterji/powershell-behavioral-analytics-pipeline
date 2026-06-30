# Solution Architecture

## Overview

The architecture was intentionally designed to be lightweight,
explainable, and suitable for enterprise production environments.

``` text
Enterprise PowerShell Logs
            │
            ▼
Python Collection Process
            │
            ▼
Hadoop (HDFS)
            │
            ▼
Feature Engineering
  • Script Length
  • Whitespace Count
            │
            ▼
Linear Regression
            │
            ▼
Residual / Outlier Analysis
            │
            ▼
Visualization & Daily Report
            │
            ▼
Threat Hunting Team
```

## Components

### Data Collection

Collect previous day's PowerShell execution logs.

### Hadoop Storage

Store and process large volumes of log data efficiently.

### Feature Engineering

Calculate behavioral metrics that distinguish normal administrative
scripts from anomalous activity.

### Statistical Analysis

Fit a regression model to characterize expected behavior and identify
significant residuals.

### Reporting

Produce visualizations and ranked outlier lists for analyst
investigation.

## Design Principles

-   Explainable analytics
-   Low computational overhead
-   Modular pipeline
-   Enterprise scalability
-   Human-in-the-loop decision making
