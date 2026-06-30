from src.feature_engineering import calculate_script_length, calculate_whitespace_count


def test_calculate_script_length():
    assert calculate_script_length("abc") == 3


def test_calculate_whitespace_count():
    assert calculate_whitespace_count("a b c") == 2
