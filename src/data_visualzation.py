import matplotlib.pyplot as plt
import seaborn as sns

def plot_monthly_revenue(monthly_df):
    plt.figure(figsize=(8, 5))
    sns.lineplot(x=monthly_df["Month"].astype(str), y=monthly_df["Revenue"], marker="o")
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue ($)")
    plt.tight_layout()
    plt.show()

def plot_top_products(top_df):
    plt.figure(figsize=(8,5))
    sns.barplot(
        x="Item Type",
        y="Revenue",
        data=top_df,
        palette="viridis",
        dodge=False,
        hue=None,
        legend=False
    )
    plt.title("Top Products by Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_regional_sales(region_df):
    plt.figure(figsize=(8,5))
    sns.barplot(
        x="Region",
        y="Revenue",
        data=region_df,
        palette="crest",
        dodge=False,
        hue=None,
        legend=False
    )
    plt.title("Revenue by Region")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

