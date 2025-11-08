import pandas as pd
import os

def load_sales_data(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found at {file_path}")
    df = pd.read_csv(file_path, parse_dates=["Date"])
    return df
