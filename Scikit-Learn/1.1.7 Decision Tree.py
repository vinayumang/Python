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