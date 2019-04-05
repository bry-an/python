from sklearn.datasets import load_boston
import mglearn
boston = load_boston()
X, y = mglearn.datasets.load_extended_boston()

print("data shape: {}".format(boston.data.shape))

mglearn.plots.plot_knn_classification(n_neighbors=1)