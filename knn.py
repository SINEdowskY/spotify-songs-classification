from classifier import Classifier
import pandas as pd

class KNN:
    def __init__(self, prediction, data, n):
        self.data = data

        self.knn = Classifier(data=self.data, n_neighbors=100)

        self.accuracy = self.knn.n_neighbors_accuracy()
        self.predi = self.knn.k_nearest_neighbors(n, prediction)

    def plot(self):
        self.knn.n_neighbors_accuracy_plot(100)
