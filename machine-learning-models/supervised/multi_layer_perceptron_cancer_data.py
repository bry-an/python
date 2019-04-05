from sklearn.neural_network import MLPClassifier
import mglearn
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
import numpy as np
cancer = load_breast_cancer()



X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=0)



mlp = MLPClassifier(random_state=52).fit(X_train, y_train)

print("Accuracy on training set: {:2f}".format(mlp.score(X_train, y_train)))
print("Accuracy on test set: {:2f}".format(mlp.score(X_test, y_test)))