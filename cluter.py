from sklearn.cluster import KMeans
import numpy as np
def getCluster(data):
    X = np.array(data)
    kmeans = KMeans(n_clusters=5, random_state=0).fit(X)

    centers = sorted(kmeans.cluster_centers_, key=lambda x: x[-1])
    for index, center in enumerate(centers):
        centers[index] = center.tolist()

    centers = centers[::-1]
    return centers
