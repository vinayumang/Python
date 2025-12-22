"""Hierarchical Clustering is an unsupervised learning technique that builds a hierarchy of clusters by either merging smaller clusters
 into larger ones (agglomerative) or splitting larger clusters into smaller ones (divisive). 
 It does not require specifying the number of clusters beforehand and produces a dendrogram,
 which is a tree-like diagram showing the sequence of merges or splits. This method is useful for understanding the structure of data and
 identifying natural groupings without assuming a fixed number of clusters."""

#Dendrogram is a tree-like diagram that illustrates the arrangement of clusters produced by hierarchical clustering.
#Scikit-learn does not have a built-in function to plot dendrograms, but we can use scipy's dendrogram function for this purpose.

import numpy as np 
import matplotlib.pyplot as plt 
from scipy.cluster.hierarchy import dendrogram , linkage
from sklearn.cluster import AgglomerativeClustering
X = np.array([[1,2],[2,1],[4,5],[5,4],[8,9]])
plt.figure(figsize = (8,5))
linked = linkage(X, method ="ward")
dendrogram(linked, orientation = 'top', distance_sort = 'descending', show_leaf_counts =True)
plt.title("Hierarchical Cluster ")
plt.show()