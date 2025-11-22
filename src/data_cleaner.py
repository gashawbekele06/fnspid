
import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean data by handling missing values and sorting by date."""
    df = df.dropna()
    df = df.sort_index()
    return df
