import numpy as np
from collections import Counter

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

def manhattan_distance(x1, x2):
    return np.sum(np.abs(x1 - x2))

def chebyshev_distance(x1, x2):
    return np.max(np.abs(x1 - x2))

class kNN:
    def __init__(self, k=3, distance_metric="euclidean"):
        self.k = k
        self.distance_metric = distance_metric
        self.distance_function = self._select_distance_function()
    
    def _select_distance_function(self):
        if self.distance_metric == "euclidean":
            return euclidean_distance
        elif self.distance_metric == "manhattan":
            return manhattan_distance
        elif self.distance_metric == "chebyshev":
            return chebyshev_distance
        else:
            raise ValueError("Invalid distance metric. Choose from 'euclidean', 'manhattan', or 'chebyshev'.")

    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        return [self._predict(x) for x in X_test]

    def _predict(self, x): 
        # Compute the distance using the selected metric
        distances = [self.distance_function(x, x_train) for x_train in self.X_train]

        # Get the k closest neighbors
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]

        # Majority vote
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]  # Return the most common label
