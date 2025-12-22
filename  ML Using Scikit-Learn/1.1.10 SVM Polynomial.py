#SVM Polynomial Kernel is used when data is not linearly separable but can be separated by a polynomial curve.
#What it does: Draws curved boundaries like parabolas (U-shape, X-shape) between classes.

#Q)Take user inputs hours & predict sucess/Failure in competition using Polynomial kernel SVM

import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split

df=pd.read_csv("Excel/SVM-Polynomial.csv")
X=df[['Hours']].values
X=df.drop("Pass",axis=1).values
y=df['Pass'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model=svm.SVC(kernel='poly',degree=3,gamma='scale') # nThis whole line means polynomial kernel with degree 3 and regularization parameter C=1.0 
model.fit(X_train,y_train)
hours=float(input("Enter hours : "))
marks=float(input("Enter marks : "))
pred = model.predict([[hours,marks]])
if pred[0]==1:
    print(" Success")
else:
    print("Failure")