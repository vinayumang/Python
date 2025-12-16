# iloc() - Accessing rows and columns by integer position and slice the data from massive data sources.

# loc() - Accessing rows and columns by labels and conditional filtering of data.

# From ProductList3.csv 
#1) Size the Row from top 2 cloumn 2 show 
#2) Show the Total price of 1st row using index

# import pandas as pd 
# df=pd.read_csv("Excel/ProductList3.csv")      
# print(df.iloc[1:2,2])    
# print(df)
# print("Slice two row and one column \ndata row")
# datacol=df.iloc[0,3]
# print('Total Price of Thread row:',datacol)


import pandas as pd 
df = pd.read_csv("Excel/ProductList3.csv")

print("=== Full DataFrame ===")
print(df)
print()

# Task 1: Get TOP 2 rows from column at index 2 (3rd column)
print("=== Top 2 rows, Column at index 2 ===")
result = df.iloc[0:2, 2]  # FIXED: 0:2 for first 2 rows
print(result)
print()

# Task 2: Get value from 1st row, column at index 3 (4th column)
print("=== First row, Column at index 3 ===")
datacol = df.iloc[0, 3]  # Row 0, Column 3
print(f'Value at row 0, column 3: {datacol}')


data={
    "name":["Vinay","Anjali","Rahul","Sneha","Kriti"],
    "marks":[85,92,78,90,88],
    "city":["Kolkata","Patna","Munger","Bengalore","Patna"]
}
df = pd.DataFrame(data)
rowdata=df.loc[0] #row 1 or A1
print(rowdata)
columndata=df.loc[:,"name"] #all rows and name column
print(columndata)