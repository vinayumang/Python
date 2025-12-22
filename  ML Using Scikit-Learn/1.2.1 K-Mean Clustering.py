#K-Mean is an unsupervised learning algorithm used for clustering data into distinct groups based on their features.
#Similar data points are grouped together in clusters, while dissimilar points are placed in different clusters.
"""
How K-Means Clustering Works:
1. Initialization: Choose the number of clusters (K) and randomly initialize K centroids.
2. Assignment Step: Assign each data point to the nearest centroid, forming K clusters.
3. Update Step: Recalculate the centroids as the mean of all data points assigned to each cluster.
4. Repeat: Repeat the assignment and update steps until the centroids no longer change significantly or a maximum number of iterations is reached.

Applications of K-Means Clustering:
1. Customer Segmentation: Grouping customers based on purchasing behavior for targeted marketing.
2. Image Compression: Reducing the number of colors in an image by clustering similar colors together.
3. Anomaly Detection: Identifying outliers in data by finding points that do not belong to any cluster.
4. Document Clustering: Organizing a large set of documents into topics based on content similarity.
Implementation with Scikit-Learn:
from sklearn.cluster import KMeans
"""

#Q)Can we group these 10 customers into 3 spending behavior types based on their annual income and spending score?"

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = {
    'customer_id':[x for x in range(1,11)],
    'age':[19,21,20,23,31,22,35,23,64,30],
    'annual_income':[15,15,16,16,17,17,18,18,19,19],
    'spending_score':[39,81,6,77,40,76,6,94,3,72]
}

df = pd.DataFrame(data) 

X = df[['annual_income','spending_score']]

model = KMeans(n_clusters=3,random_state=0)
model.fit(X)

df['cluster'] = model.labels_

print(df)

plt.scatter(X['annual_income'], X['spending_score'], c=df['cluster'])

plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.show()