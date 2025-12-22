"""
 Decision Tree is a supervised machine learning algorithm used for both classification and regression tasks.
   It works by recursively splitting the data into subsets based on feature values, creating a tree-like structure where 
   each internal node represents a decision based on a feature, each branch represents the outcome of that decision, 
   and each leaf node represents a final prediction or output.

   Basic idea
In supervised learning, the model learns from labeled examples 
(X,y)
(X,y), such as “marks + hours studied → pass/fail”.


A decision tree splits the data again and again based on feature conditions (like “marks > 40?”) until it reaches a final decision (leaf)
 such as a class label or a number.
Structure
Root node: First question/split on some feature (e.g., “Age > 18?”).
Internal nodes: Further questions based on other features (e.g., “Income > 50k?”).
Leaf nodes: Final outputs, like “Approve loan” / “Reject loan” or predicted rent value.
Types
Classification tree: Output is a category (spam / not spam, yes / no, class A / B / C).
Regression tree: Output is a continuous value (price, temperature, rent)
"""
# To predict mode with Decision Tree we needs to encode the existing dataset
#Given a person’s Age category (Junior/Youth/Middle/Senior), Income level (Low/High),
# and Credit rating (Bad/Fair/Excellent), will their loan to buy a car be approved or not?

import pandas as pd
from sklearn import tree
df=pd.read_csv("Excel/DecisionTreeDataSet.csv")
df_encode =df.apply(lambda col: col.astype('category').cat.codes) # This will encode all the categorical columns to numerical values
X = df_encode.drop("Loan_Buy_Car", axis=1).values  # Features
y = df_encode["Loan_Buy_Car"].values  # Target variable    
model = tree.DecisionTreeClassifier()
model = model.fit(X, y)
Age = input("Enter Junior/Youth/Middle/Senior:")
Income = input("Enter Low/High:")
Credit = input("Enter Fair/Good/Excellent:")
feature =[]
if Age == "Junior":
    feature.append(0)
elif Age == "Youth":
    feature.append(1)
elif Age == "Middle":
    feature.append(2)
elif Age == "Senior":
    feature.append(3)   
else:
    feature.append(0)    
if Income == "Low":
    feature.append(0)
else:
    feature.append(1)    
if Credit == "Bad":
    feature.append(0)
elif Credit == "Fair" or Credit == "Good":
    feature.append(1)
elif Credit == "Excellent":
    feature.append(2)
else:
    feature.append(0)
pred=model.predict([feature])
print("Prediction:",pred)
if pred == 0:
    print("Loan Not Approved")
else:
    print("Loan Approved")
