
import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path, parse_dates=['date'])
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()
