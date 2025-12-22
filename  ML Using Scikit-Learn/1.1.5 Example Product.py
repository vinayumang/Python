"""
Q) i> Load the data set using pandas.
ii>Prepare a module for feedback_rate & state of product using Logistic Regression.
iii> Take user input product name ,feedback_rate then predict the Sucess/Fail state of product.
iv>Also compute the accuracy of the model after the prediction 

"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# i) Load the data set using pandas
df = pd.read_csv('Excel/ProductList4.csv')   # Columns: Product_Name, Feedback_Rate, State [file:1]

# ii) Prepare a model for feedback_rate & state of product using Logistic Regression
X = df[['Feedback_Rate']]             # Feature (independent variable) [file:1]
y = df['State']                       # Target (dependent variable) [file:1]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

# iii) Take user input product name, feedback_rate then predict Success/Fail
product = input("Enter the product name: ")          # Not used in model, just for display
feedback = float(input("Enter the feedback rate: "))

prediction = model.predict([[feedback]])[0]

if prediction == 1:
    state_str = "Success"
else:
    state_str = "Fail"

print(f"The state of the product '{product}' is predicted as: {state_str}")

# iv) Compute accuracy of the model
y_pred_test = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred_test) * 100
print("Accuracy of the model: {:.2f}%".format(accuracy))




# import pandas as pd     
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score  

# df = pd.read_csv('Excel/productList4.csv')  # Load the dataset
# X = df[['feedback_rate']]  # Features
# y = df["state"]  # Target variable
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)  # Split the data
# model = LogisticRegression()  # Create the model
# model.fit(X_train, y_train)  # Train the model
# product = input("Enter the product name: ")  # User input for product name
# feedback = float(input("Enter the feedback rate: "))  # User input for feedback rate
# Success_Fail = model.predict([[feedback]])  # Predict the state
# print("The state of the product is:", Success_Fail[0])  # Output the prediction
# print("Accuracy of the model:", accuracy_score(y_test, model.predict(X_test))*100)  # Compute and print accuracy