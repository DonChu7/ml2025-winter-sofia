#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The program asks the user for input N (positive integer) and reads it.
Then the program asks the user for input k (positive integer) and reads it.
Then the program asks the user to provide N (x, y) points (one by one) and reads all of them: first: x value, then: y value for every point one by one. X and Y are the real numbers.
In the end, the program asks the user for input X and outputs: the result (Y) of k-NN Regression if k <= N, or any error message otherwise.
The basic functionality of data processing (data initialization, data insertion, data calculation) should be done using Numpy library as much as possible (note: you can combine with OOP from the previous task).
"""

import numpy as np
from sklearn.neighbors import KNeighborsRegressor

class KNNRegressorProcessor:
    def __init__(self):
        self.N = None
        self.k = None
        self.X_train = None
        self.y_train = None
        self.X_predict = None

    def get_N(self):
        while True:
            try:
                self.N = int(input("Enter N (positive integer): "))
                if self.N <= 0:
                    raise ValueError
                break
            except ValueError:
                print("N must be a positive integer. Try again.")

    def get_k(self):
        while True:
            try:
                self.k = int(input("Enter k (positive integer): "))
                if self.k <= 0:
                    raise ValueError
                if self.k > self.N:
                    print(f"Error: k cannot be larger than N ({self.N}).")
                    continue
                break
            except ValueError:
                print("k must be a positive integer. Try again.")

    def get_points(self):
        x_list = []
        y_list = []
        for i in range(self.N):
            while True:
                try:
                    x = float(input(f"Enter x for point {i+1}: "))
                    y = float(input(f"Enter y for point {i+1}: "))
                    x_list.append(x)
                    y_list.append(y)
                    break
                except ValueError:
                    print("Invalid input. Please enter real numbers.")
        self.X_train = np.array(x_list).reshape(-1, 1)
        self.y_train = np.array(y_list)

    def get_X_predict(self):
        while True:
            try:
                self.X_predict = float(input("Enter X for prediction: "))
                break
            except ValueError:
                print("Invalid input. Please enter a real number.")

    def run(self):
        self.get_N()
        self.get_k()
        self.get_points()
        self.get_X_predict()

        # Initialize and train the model
        model = KNeighborsRegressor(n_neighbors=self.k)
        model.fit(self.X_train, self.y_train)

        # Predict and display result
        y_pred = model.predict([[self.X_predict]])
        print(f"\nPredicted Y: {y_pred[0]}")

if __name__ == "__main__":
    processor = KNNRegressorProcessor()
    processor.run()