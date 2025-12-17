import pandas as pd
import numpy as np

# Real-world sales data
data = {
    'Date': pd.date_range('2024-01-01', periods=100, freq='D'),
    'Product': np.random.choice(['Laptop', 'Phone', 'Tablet', 'Watch'], 100),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 100),
    'Sales': np.random.randint(1000, 10000, 100),
    'Quantity': np.random.randint(1, 20, 100)
}

df = pd.DataFrame(data)

print("SALES ANALYSIS REPORT\n")

# 1. Total Sales by Product
print("Total Sales by Product:")
product_sales = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)
print(product_sales)
print()

# 2. Best performing region
print("Total Sales by Region:")
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print(region_sales)
print()

# 3. Monthly sales trends
df['Month'] = df['Date'].dt.month_name()
monthly_sales = df.groupby('Month')['Sales'].sum()
print("Monthly Sales:")
print(monthly_sales)
print()

# 4. Top 5 best selling days
top_days = df.groupby('Date')['Sales'].sum().nlargest(5)
print("Top 5 Best Selling Days:")
print(top_days)
