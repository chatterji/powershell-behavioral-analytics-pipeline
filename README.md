# Behavioral PowerShell Threat Detection

### Enterprise Cybersecurity Analytics Using Behavioral Feature Engineering, Statistical Anomaly Detection, and Hadoop-Based Data Processing

## Executive Summary

Modern enterprise environments generate enormous volumes of PowerShell
activity every day. The organization's SIEM platform had already filtered 
enterprise security telemetry down to approximately **50,000 daily PowerShell** 
**executions** that required further review. While this represented significant 
reduction from raw event volumes, the remaining investigation queue was still 
far beyond what security analysts could realistically investigate. Leadership 
challenged the team to determine whether AI and behavioral analytics could 
further prioritize these events into a manageable daily workload. 
Working with the organization's Red Team, two behavioral characteristics
consistently associated with malicious PowerShell scripts were
identified:

* Unusually long script length
* Unusually low whitespace density

These behavioral features were engineered into a Hadoop-based analytics
pipeline that reduced the investigation workload from **50,000+ daily
scripts** to approximately **1--2 high-risk outliers** requiring analyst
review.

\---

## Business Challenge

The organization needed to:

* Analyze all PowerShell activity daily
* Prioritize analyst investigations
* Complement existing SIEM capabilities
* Improve threat hunting efficiency
* Reduce operational risk

\---

## Solution Overview

The solution implemented a repeatable analytics workflow:

Enterprise PowerShell Logs → Python Collection → Hadoop (HDFS) → Feature
Engineering → Linear Regression → Residual Analysis → Visualization →
Threat Hunting Team

Feature Engineering consisted of:

* Script Length
* Whitespace Count

These simple but meaningful behavioral features separated normal
administrative scripts from unusual activity.

\---

## Daily Analytics Pipeline

1. Collect previous day's PowerShell logs
2. Load into Hadoop
3. Build analytical DataFrame
4. Calculate behavioral features
5. Fit regression model
6. Calculate residuals
7. Identify outliers
8. Produce analyst report

\---

## Business Results

Metric                     Before    After

\---

Daily PowerShell Scripts   800,000+  50,000+
Scripts Requiring Review   50,000+   1--2
Investigation Reduction    ---       >99.99%

\---

## Operational Benefits

* Reduced analyst workload
* Improved prioritization
* Explainable analytics
* Scalable Hadoop workflow
* Repeatable daily execution

\---

## Technologies

* Python
* Hadoop / HDFS
* pandas
* NumPy
* scikit-learn
* matplotlib

\---

## Lessons Learned

* Domain expertise drives better AI.
* Feature engineering matters more than algorithm complexity.
* Simple, explainable analytics often outperform unnecessarily complex
models.
* AI should augment analysts rather than replace them.

\---

## Future Enhancements

* Isolation Forest
* Autoencoders
* One-Class SVM
* Spark
* LLM-assisted analysis
* Explainable AI
* Real-time streaming

\---

## Confidentiality

Production logs, proprietary code, hostnames, IP addresses, and other
confidential organizational information are intentionally excluded.
Synthetic examples are used where appropriate.

\---

## About the Author

**Devin Chatterji**

AI Strategy • Enterprise Analytics • Cybersecurity Analytics • Data
Science

\---

## Key Takeaways

This repository demonstrates:

* Behavioral feature engineering
* Enterprise cybersecurity analytics
* Explainable AI
* Hadoop-based data processing
* Production-oriented analytics pipelines
* AI leadership through measurable business outcomes

> The best AI solutions are the ones that deliver measurable business
> value while remaining understandable, maintainable, and trusted.

