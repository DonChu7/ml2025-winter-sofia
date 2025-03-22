#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 17:12:49 2025

@author: dongyzhu
"""

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

class KNNOptimizerCV:
    def __init__(self):
        self.train_X = None
        self.train_y = None
        self.test_X = None
        self.test_y = None

    def _get_positive_integer(self, prompt):
        """Validate positive integer input"""
        while True:
            try:
                value = int(input(prompt))
                if value > 0: return value
                print("Must be positive. Try again.")
            except ValueError:
                print("Invalid input. Must be integer.")

    def _load_dataset(self, size, set_type):
        """Load dataset with proper validation"""
        X = np.empty(size, dtype=np.float64)
        y = np.empty(size, dtype=np.int64)
        
        for i in range(size):
            while True:
                try:
                    x_val = float(input(f"Enter X ({set_type}) for pair {i+1}: "))
                    break
                except ValueError:
                    print("Invalid X. Must be real number.")
            
            while True:
                try:
                    y_val = int(input(f"Enter Y ({set_type}) for pair {i+1}: "))
                    if y_val >= 0: break
                    print("Y must be ≥ 0.")
                except ValueError:
                    print("Invalid Y. Must be integer.")
            
            X[i] = x_val
            y[i] = y_val
        return X.reshape(-1, 1), y  # Reshape for sklearn

    def execute(self):
        # Load training data
        N = self._get_positive_integer("Enter N (training size): ")
        self.train_X, self.train_y = self._load_dataset(N, "training")

        # Load test data
        M = self._get_positive_integer("Enter M (test size): ")
        self.test_X, self.test_y = self._load_dataset(M, "test")

        # Set up grid search with cross-validation
        param_grid = {'n_neighbors': list(range(1, 11))}
        knn = KNeighborsClassifier()
        
        # Configure GridSearchCV with 5-fold cross-validation
        grid_search = GridSearchCV(
            estimator=knn,
            param_grid=param_grid,
            cv=5,
            scoring='accuracy',
            n_jobs=-1  # Use all available cores
        )

        # Perform grid search on training data
        grid_search.fit(self.train_X, self.train_y)

        # Get best model and parameters
        best_k = grid_search.best_params_['n_neighbors']
        best_model = grid_search.best_estimator_

        # Evaluate on test set
        test_pred = best_model.predict(self.test_X)
        test_acc = accuracy_score(self.test_y, test_pred)

        print(f"\nBest k: {best_k}")
        print(f"Test Accuracy: {test_acc:.4f}")

if __name__ == "__main__":
    optimizer = KNNOptimizerCV()
    optimizer.execute()