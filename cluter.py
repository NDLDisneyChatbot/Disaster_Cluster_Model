from sklearn.cluster import KMeans
import numpy as np
def getCluster(data):
    X = np.array(data)
    kmeans = KMeans(n_clusters=5, random_state=0).fit(X)
    print(kmeans.labels_)
    print(kmeans.cluster_centers_)
    return kmeans.cluster_centers_