"""RBF Kernel SVM Implementation using Scikit-Learn.
RBF draws curvy boundaries (circles/ovals) between classes when straight lines fail.
Perfect For:
Circles: Data in round clusters
Real photos/images: Faces, objects
Wavy patterns: Stock prices, weather
Most datasets: Default choice (90% cases)
"""

#Take user inputs hours attendance per predict pass/fail using RBF kernel SVM
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

# student_attendance = {
#     'hours':[3,4,7,8,6,6.5,6,9,2],
#     'attendance_per':[40, 45, 75, 80, 70, 65,50, 75,30],
#     'pass':[0, 0, 1, 0, 1, 1, 0, 1, 0]
# }

df = pd.read_csv("Excel/SVM-RBF.csv")
X = df[['Hours', 'Attendance']].values
y = df['Pass'].values      
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = svm.SVC(kernel='rbf')
model.fit(X,y)
h=float(input("Enter hours : "))
a=float(input("Enter attendance percentage : "))
feature = []
feature.append(h)
feature.append(a)
pred = model.predict([feature])
if pred[0]==1:
    print(" Pass")
else:
    print("Fail")  
pred = model.predict(x_test)
print("Accuracy : ", accuracy_score(y_test,pred))
