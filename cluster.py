from sklearn.cluster import KMeans
import numpy as np
import argparse
import ast
from sys import argv
def getCluster(data):
    data = map(float, data.strip('[]').split(','))

    X = np.array(data)
    print(X)
    kmeans = KMeans(n_clusters=5, random_state=0).fit(X)

    centers = sorted(kmeans.cluster_centers_, key=lambda x: x[-1])
    for index, center in enumerate(centers):
        centers[index] = center.tolist()

    centers = centers[::-1]
    return centers
if __name__ == '__main__':
    getCluster(argv[1])
