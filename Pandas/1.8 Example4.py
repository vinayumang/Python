#Data Cleaning & Missing Value Handling (All Industries)
#Real Use: Every data professional's first task - cleaning messy real-world data

import pandas as pd
import numpy as np

# Messy employee data with missing values
data = {
    'EmployeeID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Name': ['John', 'Sarah', 'Mike', np.nan, 'Emma', 'David', 'Lisa', 'Tom'],
    'Department': ['IT', 'HR', 'Finance', 'IT', np.nan, 'HR', 'Finance', 'IT'],
    'Salary': [50000, 60000, np.nan, 55000, 62000, 58000, np.nan, 52000],
    'Experience_Years': [5, 8, 6, np.nan, 10, 7, 9, 4],
    'Email': ['john@co.com', 'sarah@co.com', 'mike@co.com', None, 'emma@co.com', 
              'david@co.com', 'lisa@co.com', 'tom@co.com']
}

df = pd.DataFrame(data)

print("=== DATA CLEANING PROCESS ===\n")

# 1. Check missing values
print("Missing Values Count:")
print(df.isnull().sum())
print()

# 2. Fill missing numeric values with median
df['Salary'].fillna(df['Salary'].median(), inplace=True)
df['Experience_Years'].fillna(df['Experience_Years'].median(), inplace=True)

# 3. Fill missing categorical values with mode
df['Department'].fillna(df['Department'].mode()[0], inplace=True)

# 4. Drop rows with critical missing data (Name)
df.dropna(subset=['Name'], inplace=True)

print("After Cleaning - Missing Values:")
print(df.isnull().sum())
print()

# 5. Remove duplicates (if any)
df.drop_duplicates(inplace=True)

# 6. Data type conversion
df['EmployeeID'] = df['EmployeeID'].astype(str)

# 7. Create derived features
df['Salary_Per_Year_Experience'] = df['Salary'] / df['Experience_Years']

print("Cleaned Dataset:")
print(df)
print()

# 8. Summary statistics
print("Summary Statistics:")
print(df.describe())
