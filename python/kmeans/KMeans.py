#!/usr/bin/env python3
import numpy as np


def euclidDistance(point1, point2):
    return np.linalg.norm(point1 - point2)


def euclidDistanceBetweenCollections(collection1, collection2):
    """
    return: matrix len(collection1) X len(collection2)
            of distances between points in them
    """
    M = []
    for p1 in collection1:
        distances = []
        for p2 in collection2:
            distances.append(euclidDistance(p1, p2))
        M.append(distances)
    return M


def KMeans(X, k=2, max_iter=100):
    '''
    X: data (multidimensional) in np.array
    k: number of clusters
    max_iter: number of repetitions before clusters are established

    Return: tuple(
        np.array with cluster of each data point,
        np.array with mean of each cluster)

    '''
    # picking random starting  points
    randomIndexes = np.random.choice(len(X), k, replace=False)
    centroids = X[randomIndexes, :]

    # maping each point to its closest centroids
    P = np.argmin(euclidDistanceBetweenCollections(X, centroids), axis=1)

    for _ in range(max_iter):
        # calculating means of each group
        centroids = np.array([X[P == i].mean(axis=0) for i in range(k)])

        # maping each point to its closest centroids
        tmp = np.argmin(euclidDistanceBetweenCollections(X, centroids), axis=1)

        # if no change we found else continue until found/max_iter
        if np.array_equal(P, tmp):
            break
        P = tmp
    return (P, centroids)


