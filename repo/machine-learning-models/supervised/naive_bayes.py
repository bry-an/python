import numpy as np

X = np.array([[0, 1, 0, 1], [1, 0, 1, 1], [0, 0, 0, 1], [1, 0, 1, 0]])

y = np.array([0, 1, 0, 1])

for label in np.unique(y):
    print(X[y == label].sum(axis=0))