# Project Overview

## Background

Enterprise security teams routinely collect enormous quantities of
PowerShell execution data. While collection was not a problem,
prioritizing investigations was.

The organization generated more than 800,000 PowerShell execution logs every day. Existing SIEM tools successfully identified approximately 50,000 PowerShell executions that warranted additional review, making comprehensive manual investigation impractical. Existing vendor security platforms and SIEM tools could not distinguish the small number of scripts most likely to represent malicious activity.

Leadership sought an AI-assisted approach to further prioritize those events so analysts could focus on the highest-risk activity.

## Objective

Develop an explainable, scalable analytics solution that:

* Processes daily PowerShell logs
* Identifies behavioral anomalies
* Reduces analyst workload
* Integrates into an enterprise Hadoop environment

## Solution

The project focused on behavioral feature engineering rather than
signature detection.

Two measurable characteristics were extracted from every script:

1. Script Length
2. Whitespace Count

These variables were analyzed using linear regression to establish
expected script behavior. Residual analysis identified scripts that
deviated significantly from normal administrative activity.

## Outcome

The resulting workflow consistently reduced more than 50,000 daily
PowerShell scripts to approximately one or two investigation candidates,
allowing analysts to focus on the highest-risk activity while
maintaining an explainable decision process.

## Why It Matters

This project demonstrates:

* AI-enabled cybersecurity analytics
* Enterprise data engineering
* Feature engineering
* Statistical anomaly detection
* Production workflow design
* Measurable business impact

