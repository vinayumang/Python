#Focus karta hai data analysis aur manipulation libraray on tabular and labeled data similar to excel or SQL tables.
#It provides data structures like Series (1D) and DataFrame (2D) for handling and analyzing data efficiently.

#Main practical uses are importing data from CSV,Excel,SQL ,Json etc into DataFrames for analysis.
#cleaning and transforming data by handling missing values, filtering, grouping, and aggregating.

#Analysis and ML Workflow like calculating mean,min,max,correlations and group wise aggregations.
#Preparing datasets for machine learning by cleaning ,encoding,reshaping and exporting to other libraries
#  like scikit-learn or TensorFlow.

# It integrates well with other libraries like NumPy for numerical operations, Matplotlib and Seaborn for data visualization.


# Series  : 1D labeled array capable of holding any data type.
# DataFrame : Multidimensional labeled data structure with columns of potentially different types.

import pandas as pd

a=[10,20,30,40,50]
myvar=pd.Series(a)
print(myvar) # prints the Series with default integer index

data ={
    "Student":["Vinay","Rahul","Mayank","Ankit","Aniket",],  # 2-D data for DataFrame
    "Marks":[90,85,88,88,92]
}
df=pd.DataFrame(data)
print(df) # prints the DataFrame with default integer index