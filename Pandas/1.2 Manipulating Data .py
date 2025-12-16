# Load the Product.csv into a DataFrame
#create a new column "Total_Price"
#Find the sum and mean of Total_Price column

import pandas as pd
df = pd.read_csv('Excel/Product.csv') 
print(df)  # Display the DataFrame  
print(df.info())  # Display concise summary of the DataFrame
df['Total_Price'] = df['Qty'] * df['Price']
#save the modified DataFrame to a new CSV file
df.to_csv('Excel/Product.csv')
df1 = pd.read_csv('Excel/Product.csv')
sum_total_price = df1['Total_Price'].sum()
mean_total_price = df1['Total_Price'].mean()
print("Sum of Total_Price:", sum_total_price)
print("Mean of Total_Price:", mean_total_price) 
cummax_total_price = df1['Total_Price'].cummax()
print("Cumulative Maximum of Total_Price:\n", cummax_total_price)

