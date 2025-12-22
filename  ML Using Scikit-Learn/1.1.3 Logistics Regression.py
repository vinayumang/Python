"""
Logistics Regression: A machine learning algorithm used for binary classification tasks. 
It models the probability of a binary outcome based on one or more predictor variables using the logistic function.
from sklearn.model_selection import train_test_split
Train_test_split: A function in Scikit-Learn that divides a dataset into training data and testing data.

1)training data is used to train the model, 
2)while testing data is used to evaluate its performance.

X dataSet in 2D array
y dataSet in 1D array
test_size: proportion of the dataset to include in the test split (e.g., 0.2 for 20%).
random_state: seed used by the random number generator for reproducibility.
"""
# Program mai abhi ke liye dikkat hai

#Q Data 
# task_hr(X) =	15	18	25	23	28	24.5	40	35	32	5
# y =	0	0	1	0	1	1	0	1	1	0
#Take user input "task-hr" and by using logistics regression check sucess or failure
#Formula:train_test_split(X, y, test_size=0.2, random_state=42) we use random_state=42 because it is commonly used as a standard for reproducibility in examples and tutorials.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Create dataset
data = {'task_hr': [15, 18, 25, 23, 28, 24.5, 40, 35, 32, 5],
        'y': [0, 0, 1, 0, 1, 1, 0, 1, 1, 0]}
df = pd.DataFrame(data)

# Separate features and target
X = df[['task_hr']]
y = df['y']

# Split data into training (80%) and testing (20%)
# random_state=42 ensures reproducibility - same split every time
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model on training data only
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate model accuracy on test data
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Get user input and predict
task_hr = float(input("Enter task hours: "))
input_df = pd.DataFrame({'task_hr': [task_hr]})
pred = model.predict(input_df)

# Display result
if pred[0] == 1:
    print(f"Task Hours: {task_hr} → Prediction: Success (1)")
else:
    print(f"Task Hours: {task_hr} → Prediction: Failure (0)")


# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score  

# data = {'task_hr': [15, 18, 25, 23, 28, 24.5, 40, 35, 32, 5],
#         'y': [0, 0, 1, 0, 1, 1, 0, 1, 1, 0]}
# df = pd.DataFrame(data)
# X = df[['task_hr']]
# y = df['y']     
# model = LogisticRegression()
# model.fit(X, y)
# task_hr = float(input("Enter task hours: "))
# pred=model.predict([[task_hr]])
# print("output:",pred[0])