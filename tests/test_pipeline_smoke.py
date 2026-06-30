from pathlib import Path

from src.generate_sample_data import generate_sample_data


def test_generate_sample_data(tmp_path):
    output_file = tmp_path / "sample.csv"
    df = generate_sample_data(output_file=output_file, sample_size=25, outlier_count=2)

    assert output_file.exists()
    assert len(df) == 25
    assert "script_text" in df.columns
