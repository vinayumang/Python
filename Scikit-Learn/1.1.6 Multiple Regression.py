"""Multile Regression is a statistical technique that uses multiple explanatory variables to predict the outcome of a response variable. 
The goal of multiple regression is to model the relationship between the explanatory and 
response variables, allowing for more accurate predictions and insights into how different factors influence the outcome."""
#Example:Dataset for people area in sq.ft,age,income by using multiple regression predict the rent input required area age and income of people

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df=pd.read_csv('Excel/Rent.csv') 
X=df.drop("Rent",axis=1).values
y=df["Rent"].values                       #.values if we dont have feature name otherwise it gives Warning in output
model=LinearRegression()
model.fit(X,y)
area=float(input("Enter the area in sq.ft: "))
age=int(input("Enter the age of the house: "))
income=float(input("Enter the income of the people: "))      #other way for Feature name warning X_new = pd.DataFrame([[area, age, income]], columns=["Area", "Age", "Income"])
pred_rent=model.predict([[area,age,income]])                      #rent = model.predict(X_new)
print("The predicted rent is: ",pred_rent[0])






""" 
# ... after fitting the model as you already did ...

area = float(input("Enter the area in sq.ft: "))
age = int(input("Enter the age of the house: "))
income = float(input("Enter the income of the people: "))

# Create a one-row DataFrame with correct column names
X_new = pd.DataFrame([[area, age, income]], columns=["Area", "Age", "Income"])
rent = model.predict(X_new)
print("The predicted rent is:", rent[0])

"""

