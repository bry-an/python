from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import mglearn
import numpy as np
from sklearn.svm import LinearSVC


X, y = make_blobs(random_state=42)
mglearn.discrete_scatter(X[:,0], X[:,1], y)
plt.xlabel("Feature 0")
plt.ylabel("Feature 1")
# plt.legend(["class 0", "class 1", "class 2"])
# plt.show()
linear_svm = LinearSVC().fit(X, y)

line = np.linspace(-15, 15)
for coef, intercept, color in zip(linear_svm.coef_, linear_svm.intercept_, mglearn.cm3.colors):
    plt.plot(line, -(line * coef[0] + intercept) / coef[1], c=color)
plt.ylim(-10, 15)
plt.xlim(-10, 8)

plt.legend(["class 0", "class 1", "class 2", "line class 0", "line class 1", "line class 2"], loc=(1.01, 0.3))
plt.show()