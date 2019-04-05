from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
import mglearn
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
import numpy as np

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=0)

# default is 100 trees and a learning rate of 0.1
grbt = GradientBoostingClassifier(random_state=0)
grbt.fit(X_train, y_train)

print("Accuracy on training set: {}".format(grbt.score(X_train, y_train))) # 1.00
print("Accuracy on test set: {}".format(grbt.score(X_test, y_test))) # 0.958

# apply stronger pre-pruning by limiting the max depth or lowering the learning rate

grbt2 = GradientBoostingClassifier(random_state=0, max_depth=1)
grbt2.fit(X_train, y_train)

print("Accuracy on pruned training set: {}".format(grbt2.score(X_train, y_train))) # 0.991
print("Accuracy on pruned test set: {}".format(grbt2.score(X_test, y_test))) # 0.972

grbt3 = GradientBoostingClassifier(random_state=0, learning_rate=0.01)
grbt3.fit(X_train, y_train)

print("Accuracy on pruned training set: {}".format(grbt3.score(X_train, y_train))) # 0.988
print("Accuracy on pruned test set: {}".format(grbt3.score(X_test, y_test))) # 0.965


