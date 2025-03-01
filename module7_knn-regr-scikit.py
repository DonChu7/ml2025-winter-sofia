import numpy as np
from sklearn.neighbors import KNeighborsRegressor

class KNNRegressionProcessor:
    def __init__(self):
        self.N = None
        self.k = None
        self.X_train = None
        self.y_train = None
        self.X_predict = None
        self.variance = None

    def get_N(self):
        while True:
            try:
                self.N = int(input("Enter N (positive integer): "))
                if self.N <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. N must be a positive integer.")

    def get_k(self):
        while True:
            try:
                self.k = int(input("Enter k (positive integer): "))
                if self.k <= 0 or self.k > self.N:
                    print(f"Error: k must be positive and <= {self.N}")
                    continue
                break
            except ValueError:
                print("Invalid input. k must be a positive integer.")

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
        self.variance = np.var(self.y_train)

    def get_X_predict(self):
        while True:
            try:
                self.X_predict = float(input("Enter X for prediction: "))
                break
            except ValueError:
                print("Invalid input. Please enter a real number.")

    def run_regression(self):
        model = KNeighborsRegressor(n_neighbors=self.k)
        model.fit(self.X_train, self.y_train)
        return model.predict([[self.X_predict]])[0]

    def execute(self):
        self.get_N()
        self.get_k()
        self.get_points()
        self.get_X_predict()
        
        try:
            y_pred = self.run_regression()
            print(f"\nPredicted Y: {y_pred:.4f}")
            print(f"Variance of training labels: {self.variance:.4f}")
        except ValueError as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    processor = KNNRegressionProcessor()
    processor.execute()