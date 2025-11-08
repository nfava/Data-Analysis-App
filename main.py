import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
from src.data_loader import load_sales_data
from src.data_analysis import (
    add_revenue_column,
    get_summary_stats,
    monthly_revenue,
    top_products,
    regional_sales
)
from src.data_visualzation import (
    plot_monthly_revenue,
    plot_top_products,
    plot_regional_sales, plot_order_shiptime
)

def main():
    # Load data
    df = load_sales_data("data/100 Sales Records.csv")
    df = add_revenue_column(df)

    # Print stats
    print("📊 Sales Summary Statistics:")
    print(get_summary_stats(df))
    print("\nTop Products by Revenue:")
    print(top_products(df))
    print("\nRegional Sales:")
    print(regional_sales(df))

    # Generate plots
    plot_monthly_revenue(monthly_revenue(df))
    plot_top_products(top_products(df))
    plot_regional_sales(regional_sales(df))
    plot_order_shiptime(df)
if __name__ == "__main__":
    main()