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

#Q) Inputs are from user end and compute rent based on area using Linear Regression

import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([[1000], [750], [1000], [1250], [1500], [1750], [2000]])  #why extra brackets? because sklearn expects 2D array for features
y = np.array([4000, 2000, 2500, 3000, 3500, 4000, 4500])    #why single bracket? because target variable is 1D array
model = LinearRegression()  
model.fit(x, y)
area = float(input("Enter the area of the house in sq ft: "))
price = model.predict([[area]])
print(f"Area in SqFt: {area}, Price: {price[0]}")