#Time Series Analysis (Energy & Finance)
#Real Use: Energy companies track usage patterns; financial firms analyze stock prices.

import pandas as pd
import numpy as np

# Time series energy usage data
dates = pd.date_range('2024-01-01', periods=30, freq='D')
data = {
    'Date': dates,
    'Energy_Usage_kWh': np.random.randint(80, 200, 30),
    'Temperature': np.random.randint(15, 35, 30),
    'Peak_Hour_Usage': np.random.randint(20, 50, 30)
}

df = pd.DataFrame(data)
df.set_index('Date', inplace=True)

print("=== ENERGY USAGE TIME SERIES ANALYSIS ===\n")

# 1. Daily statistics
print("Daily Usage Statistics:")
print(df['Energy_Usage_kWh'].describe())
print()

# 2. Weekly averages
weekly_avg = df['Energy_Usage_kWh'].resample('W').mean()
print("Weekly Average Usage:")
print(weekly_avg)
print()

# 3. Find peak usage days
print("Top 5 Peak Usage Days:")
peak_days = df.nlargest(5, 'Energy_Usage_kWh')
print(peak_days)
print()

# 4. Correlation between temperature and usage
correlation = df['Temperature'].corr(df['Energy_Usage_kWh'])
print(f"Correlation between Temperature and Energy Usage: {correlation:.2f}")
print()

# 5. Rolling 7-day average
df['7Day_Avg'] = df['Energy_Usage_kWh'].rolling(window=7).mean()
print("Recent 7-Day Rolling Averages:")
print(df[['Energy_Usage_kWh', '7Day_Avg']].tail(10))
