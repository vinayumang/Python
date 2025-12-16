import pandas as pd
df = pd.read_csv('Excel/Pizza.csv')  # Replace 'data.csv' with your CSV file path
print(df)  # Display the DataFrame  

print("--- Divider ")
print(df.head())  # Display the first 5 rows of the DataFrame
print(df.head(5))  # Display the first 5 rows of the DataFrame
print("--- Divider ")
print(df.tail())  # Display the last 5 rows of the DataFrame
print(df.tail(3))  # Display the last 3 rows of the DataFrame
print(df.describe())  # Display     statistical summary of numerical columns
print(df.info())  # Display concise summary of the DataFrame
print(df.columns)  # Display the column names of the DataFrame
print(df.shape)  # Display the shape (rows, columns) of the DataFrame
print(df.dtypes)  # Display the data types of each column   


#Loading Specifics columns
df_specific = pd.read_csv('Excel/Pizza.csv', usecols=['Diameter', 'Price'])  # Load only 'Diameter' and 'Price' columns
print(df_specific)

#sum() function to get total price or sum of selected column
total_price = df['Price'].sum()
print("Total Price:", total_price)