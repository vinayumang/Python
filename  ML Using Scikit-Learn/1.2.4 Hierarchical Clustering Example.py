import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

df = pd.read_csv("Excel/HierarchicalClustering.csv")
print(df)
df1 = df[['Income','Expense']]
X = np.array(df1)
plt.figure(figsize=(8,5))
linked = linkage(X, method ='ward')
dendrogram = dendrogram(linked,orientation= 'top', show_leaf_counts =True)

plt.xlabel("Data Merge Point")
plt.ylabel("Difference Income / Expense")
plt.title("Organisation Income/ Expense Dendrogram")
plt.show()