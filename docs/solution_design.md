# Solution Design

The solution emphasized **behavioral feature engineering** rather than
signature matching.

## Design Principles

-   Explainable analytics
-   Low computational cost
-   Daily batch execution
-   Enterprise scalability
-   Human-in-the-loop investigation

Two engineered features---script length and whitespace count---were
extracted from each PowerShell script and analyzed using linear
regression to identify anomalous behavior.
