import pandas as pd

from src.config import SCRIPT_LENGTH_COLUMN, WHITESPACE_COUNT_COLUMN
from src.regression_model import add_regression_outputs, fit_behavioral_regression


def test_regression_model_adds_outputs():
    df = pd.DataFrame(
        {
            SCRIPT_LENGTH_COLUMN: [100, 200, 300],
            WHITESPACE_COUNT_COLUMN: [10, 20, 30],
        }
    )
    model = fit_behavioral_regression(df)
    scored = add_regression_outputs(df, model)

    assert "predicted_whitespace_count" in scored.columns
    assert "residual" in scored.columns
