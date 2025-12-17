# CSV/Excel Data Import & Export (Business Reporting)
#Real Use: Companies merge data from multiple sources for reports and dashboards

import pandas as pd

# Program to merge data from multiple sources and export reports

# Dataset 1: Employee Information
employees = pd.DataFrame({
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['John', 'Sarah', 'Mike', 'Emma', 'David'],
    'Department': ['IT', 'HR', 'Finance', 'IT', 'HR']
})

# Dataset 2: Salary Information
salaries = pd.DataFrame({
    'EmployeeID': [101, 102, 103, 104, 105],
    'Base_Salary': [50000, 60000, 55000, 62000, 58000],
    'Bonus': [5000, 6000, 5500, 6200, 5800]
})

# Dataset 3: Performance Ratings
performance = pd.DataFrame({
    'EmployeeID': [101, 102, 103, 104, 105],
    'Rating': [4.2, 4.8, 3.9, 4.5, 4.3],
    'Projects_Completed': [8, 12, 6, 10, 9]
})

print("=== DATA INTEGRATION & REPORTING ===\n")

# 1. Merge all datasets
merged_df = employees.merge(salaries, on='EmployeeID')
merged_df = merged_df.merge(performance, on='EmployeeID')

# 2. Calculate total compensation
merged_df['Total_Compensation'] = merged_df['Base_Salary'] + merged_df['Bonus']

# 3. Performance categories
merged_df['Performance_Category'] = pd.cut(merged_df['Rating'], 
 bins=[0, 4.0, 4.5, 5.0],
labels=['Needs Improvement', 'Good', 'Excellent'])

print("Integrated Employee Report:")
print(merged_df)
print()

# 4. Department-wise statistics
print("Department-wise Analysis:")
dept_stats = merged_df.groupby('Department').agg({
    'Total_Compensation': 'mean',
    'Rating': 'mean',
    'Projects_Completed': 'sum'
}).round(2)
print(dept_stats)
print()

# 5. Export to different formats
# merged_df.to_csv('employee_report.csv', index=False)
# merged_df.to_excel('employee_report.xlsx', index=False)
print("✓ Data ready for export to CSV/Excel")

# 6. Filter and export high performers
high_performers = merged_df[merged_df['Rating'] >= 4.5]
print(f"\nHigh Performers ({len(high_performers)}):")
print(high_performers[['Name', 'Department', 'Rating', 'Total_Compensation']])
