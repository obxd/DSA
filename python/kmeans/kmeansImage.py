#!/usr/bin/env python3
import time
import numpy as np
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
from importlib import reload
from KMeans import KMeans


def make_feature_scalers(x):
    _min = np.array([v[i] for i, v in enumerate(x[np.argmin(x, axis=0)])])
    _max = np.array([v[i] for i, v in enumerate(x[np.argmax(x, axis=0)])])

    def scale(x):
        return (x - _min) / (_max - _min)

    def deScale(x):
        return (_max - _min) * x + _min

    return scale, deScale


def replaceWithCentroid(clustered_pixels, centroids):
    new_pixels = []
    for c in clustered_pixels:
        new_pixels.append(centroids[c])
    return np.array(new_pixels)


if __name__ == "__main__":

    img = Image.open('wp.png')
    ori_pixels = np.asarray(img)
    shape = ori_pixels.shape
    ori_pix_arr = ori_pixels.reshape(shape[0]*shape[1], 3)
    scale, deScale = make_feature_scalers(ori_pix_arr)

    start = time.time()
    print("scaling:")
    scaled_ori_pix_arr = scale(ori_pix_arr)
    print(time.time() - start)

    start = time.time()
    print("clastering:")
    (clustered, centroids) = KMeans(scaled_ori_pix_arr, k=8)
    print(time.time() - start)

    print("---------------------")
    print(centroids)
    print("---------------------")

    start = time.time()
    print("descaling:")
    descaled_centroids = deScale(centroids)
    print(time.time() - start)

    print("---------------------")
    print(descaled_centroids)
    print("---------------------")

    start = time.time()
    print("floor:")
    centroid_pixels = np.floor(descaled_centroids)
    print(time.time() - start)

    print("---------------------")
    print(centroid_pixels)
    print("---------------------")

    start = time.time()
    print("replacing pixels:")
    new_pixels = replaceWithCentroid(clustered, centroid_pixels)
    print(time.time() - start)

    print("---------------------")
    print(new_pixels[:10])
    print("---------------------")

    pilImage = Image.fromarray(new_pixels.reshape(*shape).astype(np.uint8))
    plt.imshow(pilImage)
    plt.show()
