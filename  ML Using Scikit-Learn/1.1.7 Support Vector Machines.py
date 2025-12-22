"""Introduction to Support Vector Machines (SVM) using Scikit-Learn.
 SVM is a powerful supervised machine learning algorithm used for classification and regression tasks.
 It works by finding the optimal hyperplane that separates data points of different classes in a high-dimensional space.
 
 SVM identifies the hyperplane that maximizes the distance to the nearest data points from each class, 
 known as the hard margin approach for linearly separable data. For non-linear data, kernel functions transform the 
 input space into a higher-dimensional one where separation becomes feasible
 Uses: 
- Text classification
- Image classification
- Bioinformatics (e.g., gene classification)
- Handwriting recognition
- Face detection

SVM Types:
- Linear SVM: Used for linearly separable data.
- Non-linear SVM: Uses kernel functions (like RBF, polynomial) to handle non-linear data.
"""
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import svm
# x = [[2,3],[3,4],[1,1],[5,6],[6,7],[4,3],[6,8]]
# y = [0,0,0,1,1,0,1]
df=pd.read_csv("Excel/SVM-LinearKernalFunction.csv")
x=df[['X','Y']].values
y=df['Class'].values
model = svm.SVC(kernel='linear')
model.fit(x,y)
x1 = int(input("Enter x cordinate : "))
y1 = int(input("Enter the y coordinate : "))
feature =[]
feature.append(x1)
feature.append(y1)
pred = model.predict([feature])
print("class purpose by model : ",pred[0])
for i, point in enumerate(x):
    if y[i] == 0:
        plt.scatter(point[0], point[1],marker ='o')
    else:
        plt.scatter(point[0],point[1], marker='s')

plt.title("Linear Scatter ")
plt.xlabel("x")
plt.ylabel('class')
plt.show()