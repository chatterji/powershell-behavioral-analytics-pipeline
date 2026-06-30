# Executive Summary

## Overview

This repository presents an enterprise cybersecurity analytics solution
that applies behavioral feature engineering and statistical anomaly
detection to PowerShell activity.

The solution was developed to address a real operational problem: more
than **800,000 PowerShell execution logs were generated daily**. Existing

SIEM tools successfully identified approximately **50,000 PowerShell**

**executions** that warranted additional review, making comprehensive manual

investigation impractical. Leadership sought an AI-assisted approach to

further prioritize those events so analysts could focus on the highest-risk

activity.

Working with a member of the organization's Red Team, two behavioral
indicators of malicious PowerShell scripts were identified:

* Script length
* Whitespace density

These features were engineered into a lightweight Python/Hadoop
analytics pipeline that consistently reduced the investigation queue to
approximately **1--2 high-risk scripts per day**.

## Business Value

* Reduced investigation workload by more than 99.99%
* Enabled focused threat hunting
* Complemented existing SIEM capabilities
* Demonstrated explainable AI for cybersecurity
* Produced a repeatable production analytics workflow

## Key Technologies

* Python
* Hadoop / HDFS
* pandas
* scikit-learn
* matplotlib
* Behavioral feature engineering
* Linear regression
* Residual analysis

> The value of this solution came from combining cybersecurity domain
> knowledge with practical, explainable analytics to solve an
> enterprise-scale operational problem.

