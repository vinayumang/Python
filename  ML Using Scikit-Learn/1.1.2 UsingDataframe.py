"""Program to take 10 students study hour and obtained marks and store them in a dataframe using pandas library 
and compute marks for given study hours"""

import pandas as pd
from sklearn.linear_model import LinearRegression

data={
    'Hours':[2.5,5.1,3.2,8.5,7.4,2.2,4.5,3.6,6.1,7.6],
    'Marks':[21,47,27,75,62,20,52,30,60,70]
}
df=pd.DataFrame(data)
X=df[['Hours']]
y=df['Marks']
model=LinearRegression()
model.fit(X,y)
inputhours = float(input("Enter the study hours: "))
input_df = pd.DataFrame({'Hours': [inputhours]})
marks_predict = model.predict(input_df)
print("Predicted marks for given study hours is:",inputhours)
print(f"Study Hours: {inputhours}, Predicted Marks: {marks_predict[0]}")


#Warning :X does not have valid feature names, but LinearRegression was fitted with feature names
"""
Warning Explanation:    
This warning occurs because the input provided to the predict method does not match the feature names used during the model training. 
In this case, the model was trained using a DataFrame with a column named 'Hours', but the input was provided as a simple list or array without specifying the feature name.
To avoid this warning, ensure that the input to the predict method is in the same format as the training data, including the feature names.

The problem: You created input_df correctly but then didn't use it. You still passed [[inputhours]] to predict(), which is why the warning appeared.

inputhours=float(input("Enter the study hours: "))
marks_predict=model.predict([[inputhours]]) #Warning :X does not have valid feature names, but LinearRegression was fitted with feature names
"""

