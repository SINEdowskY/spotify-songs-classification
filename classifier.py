import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from IPython import display
from spotify_data import SpotifyData
from genres import get_genres


class Classifier:
    def __init__(self, data, n_neighbors):
        self.data = data
        self.n_neighbors = n_neighbors

        self.__X = self.data.iloc[:, 2:len(data)]
        self.__y = self.data.genre
        self.__X_train, self.__X_test, self.__y_train, self.__y_test = train_test_split(
            self.__X, self.__y, random_state=0, shuffle=True
        )

    def n_neighbors_accuracy(self):
        check_best_n = []

        for i in range(1, self.n_neighbors, 2):
            knn = KNeighborsClassifier(n_neighbors=i)
            knn.fit(self.__X_train, self.__y_train)
            score = knn.score(self.__X_test, self.__y_test)
            check_best_n.append(score * 100)
        return check_best_n

    def n_neighbors_accuracy_plot(self, max_n):
        nn_accuracy = self.n_neighbors_accuracy()
        x_plot = [i for i in range(1, len(nn_accuracy) + 1)]
        y_plot = nn_accuracy
        plt.plot(x_plot, y_plot)
        self.__annot_max(x_plot, y_plot)
        plt.xlabel("index ilosci sasiadow w liscie")
        plt.ylabel("% precyzji knn")
        plt.title("wykres ilosci sasiadow i precyzji algorytmu")
        plt.show()

    def k_nearest_neighbors(self, n, data_to_predict):
        knn = KNeighborsClassifier(n_neighbors=n)
        knn.fit(self.__X_train, self.__y_train)
        return knn.predict(data_to_predict)


    def __annot_max(self, x, y, ax=None):
        xmax = x[np.argmax(y)]
        ymax = max(y)
        text = "x={:.3f}, y={:.3f}".format(xmax, ymax)
        if not ax:
            ax = plt.gca()
        bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
        arrowprops = dict(arrowstyle="->", connectionstyle="angle,angleA=0,angleB=60")
        kw = dict(xycoords='data', textcoords="axes fraction",
                  arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
        ax.annotate(text, xy=(xmax, ymax), xytext=(0.94, 0.96), **kw)
