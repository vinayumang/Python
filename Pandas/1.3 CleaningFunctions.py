# Cleaning : Handling missing values, duplicates, and inconsistent data entries in a DataFrame.
#Functions like dropna(), fillna(), replace(), and duplicated() are commonly used for data cleaning tasks.
#syntax : df1=df.dropna(),df1= df.fillna(value), df1=df.replace(to_replace, value),df1= df.duplicated()

import pandas as pd
df = pd.read_csv('Excel/ProductList2.csv')  # Load the CSV file into a DataFrame
print(df)  # Display the original DataFrame

#Finding null values
df1=df.isnull()
print("Null Values in DataFrame:\n", df1)

#fillna() : Fill missing values with a specified value
df2=df.fillna(0)
print("DataFrame after filling missing values with 0:\n", df2)  

#dropna() : Drop rows with any missing values
df3=df.dropna()
print("DataFrame after dropping rows with missing values:\n", df3)  

#drop_duplicates() : Remove duplicate rows
df4=df.drop_duplicates()
print("DataFrame after removing duplicate rows:\n", df4)
