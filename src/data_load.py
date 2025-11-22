
import pandas as pd
from pathlib import Path


def load_csv_file(file_path):
    """
    Load a single stock CSV file into a pandas DataFrame.
    Detects date column dynamically and validates required columns.
    """
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    df = pd.read_csv(file_path)

    # Detect date column dynamically
    possible_date_cols = ['date', 'datetime', 'timestamp']
    date_col = None
    for col in df.columns:
        if col.strip().lower() in possible_date_cols:
            date_col = col
            break

    if not date_col:
        raise KeyError(f"No date column found in {file_path.name}. Columns: {df.columns.tolist()}")

    # Convert and clean
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df = df[df[date_col].notna()].sort_values(date_col)
    df.set_index(date_col, inplace=True)

    # Normalize column names
    df = df.rename(columns=lambda x: x.strip().title())

    # Validate required columns
    required_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
    if not all(col in df.columns for col in required_cols):
        raise ValueError(f"Missing columns in {file_path.name}. Found: {df.columns.tolist()}")

    return df
