#Customer Churn Analysis (Banking & Subscriptions)
#Real Use: Netflix, banks, and SaaS companies predict which customers might leave
import pandas as pd

# Customer behavior data
data = {
    'CustomerID': range(1, 11),
    'Age': [25, 45, 35, 50, 28, 42, 38, 55, 30, 48],
    'Tenure_Months': [12, 48, 24, 60, 6, 36, 18, 72, 3, 54],
    'Monthly_Charges': [50, 80, 65, 100, 45, 75, 60, 110, 40, 95],
    'Total_Charges': [600, 3840, 1560, 6000, 270, 2700, 1080, 7920, 120, 5130],
    'Churned': [0, 0, 0, 0, 1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

print("=== CUSTOMER CHURN ANALYSIS ===\n")

# 1. Churn rate
churn_rate = (df['Churned'].sum() / len(df)) * 100
print(f"Overall Churn Rate: {churn_rate:.1f}%\n")

# 2. Compare churned vs retained customers
print("Average Metrics by Churn Status:")
churn_comparison = df.groupby('Churned')[['Age', 'Tenure_Months', 'Monthly_Charges']].mean()
churn_comparison.index = ['Retained', 'Churned']
print(churn_comparison)
print()

# 3. Identify high-risk customers (low tenure + high charges)
high_risk = df[(df['Tenure_Months'] < 12) & (df['Monthly_Charges'] > 60)]
print(f"High Risk Customers (Low Tenure + High Charges): {len(high_risk)}")
print(high_risk[['CustomerID', 'Tenure_Months', 'Monthly_Charges', 'Churned']])
print()

# 4. Customer lifetime value
df['Avg_Monthly_Value'] = df['Total_Charges'] / df['Tenure_Months']
print("Top 5 Customers by Average Monthly Value:")
print(df.nlargest(5, 'Avg_Monthly_Value')[['CustomerID', 'Avg_Monthly_Value']])
