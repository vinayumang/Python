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

