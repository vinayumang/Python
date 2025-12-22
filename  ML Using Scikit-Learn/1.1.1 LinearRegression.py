#Linear Regression is used for predicting a continuous target variable based on one or more predictor variables.
#It assumes a linear relationship between the input variables (features) and the output variable (target).
#Importing necessary libraries

#Linear Regression compute the linear straight line that best fits the data points. y = mx + c,where y is the target variable, x is the feature, m is the slope, and c is the y-intercept.

# fit() - Teaches the model by finding the best line from training data
# After fit(), the model knows the pattern (slope & intercept)

# predict() - Uses the learned pattern to guess answers for new data
# Just applies the formula, no learning happens

# score() - Checks how accurate the model is (R² score)
# Close to 1 = good predictions, close to 0 = poor predictions

"""Q) Inputs are from user end and compute rent based on area using Linear Regression"""

import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1000], [1200], [700], [650], [1800],[2000]])  #why extra brackets? because sklearn expects 2D array for features also apply while importing csv file
y = np.array([4000, 4500,3500, 2500, 5500, 5300])    #why single bracket? because target variable is 1D array
model = LinearRegression()  
model.fit(X, y)
area = float(input("Enter the area of the house in sq ft: "))
price = model.predict([[area]])
print(f"Area in SqFt: {area}, Price: {price[0]}")


#Alternative way using pandas to read data from csv file
#from sklearn.linear_model import LinearRegression
#import pandas as pd
# Read data from CSV file
# df = pd.read_csv('house_data.csv')
# Separate features (X) and target (y)
# X = df[['Area']]  # Double brackets keep it as DataFrame (2D)
# y = df['Rent']     # Single bracket makes it a Series (1D)
# Create and train the model
# model = LinearRegression()
# model.fit(X, y)
# Get user input and predict
# area = float(input("Enter the area of the house in sq ft: "))
# price = model.predict([[area]])  # Double brackets for 2D array
# print(f"Area in SqFt: {area}, Price: {price[0]}")