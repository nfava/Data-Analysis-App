import pandas as pd

def add_revenue_column(df: pd.DataFrame) -> pd.DataFrame:
    df["Revenue"] = df["Units Sold"] * df["UnitPrice"]
    return df

def get_summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe()

def monthly_revenue(df: pd.DataFrame) -> pd.DataFrame:
    df["Month"] = df["Date"].dt.to_period("M")
    return df.groupby("Month")["Revenue"].sum().reset_index()

def top_products(df: pd.DataFrame, n=3) -> pd.DataFrame:
    return df.groupby("Product")["Revenue"].sum().nlargest(n).reset_index()

def regional_sales(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("Region")["Revenue"].sum().reset_index()
