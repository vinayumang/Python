#Email Spam Detection using Logistic Regression

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Sample email data: word_count, special_chars, links
data = {
    'word_count': [50, 200, 30, 150, 80, 300, 45, 120, 90, 250],
    'special_chars': [5, 15, 2, 20, 8, 25, 3, 12, 7, 18],
    'links': [0, 3, 0, 5, 1, 8, 0, 2, 1, 6],
    'is_spam': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]  # 0=Not Spam, 1=Spam
}
df = pd.DataFrame(data)

X = df[['word_count', 'special_chars', 'links']]
y = df['is_spam']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

# Test accuracy
y_pred = model.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")

# Predict for new email
word_count = int(input("Enter word count: "))
special_chars = int(input("Enter special character count: "))
links = int(input("Enter number of links: "))

new_email = pd.DataFrame({'word_count': [word_count],'special_chars': [special_chars],'links': [links]})
prediction = model.predict(new_email)

print(f"Prediction: {'SPAM' if prediction[0] == 1 else 'NOT SPAM'}")
