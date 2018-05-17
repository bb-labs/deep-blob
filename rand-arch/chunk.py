from sklearn.datasets import fetch_mldata
from math import sin, pi, tan, cos, inf

import matplotlib.pyplot as plt
import numpy as np

mnist = fetch_mldata('MNIST original')


def index_list(data):
    indices = np.indices(data.shape)
    return np.vstack([
        indices[i].ravel() for i in range(len(indices))
    ]).T


def rand_rect(max_area):
    w = np.random.randint(max_area) + 1
    h = int(max_area / w)

    return (w, h)


def chunk_input(data):
    indices = index_list(data)
    r_indxs = list(np.random.choice(
        len(indices), size=len(indices), replace=False))

    chunks = []
    while r_indxs:
        area = np.random.randint(len(r_indxs))
        w, h = rand_rect(area + 1)

        chunk = np.array([data[tuple(indices[r_indxs.pop()])]
                          for _ in range(w * h)])

        chunks.append(chunk.reshape(w, h))

    return chunks


a = np.random.randn(5, 5, 3)
chunks = chunk_input(a)
