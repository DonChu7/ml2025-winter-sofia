#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 13:07:15 2025

@author: dongyzhu
"""

import numpy as np
from sklearn.metrics import precision_score, recall_score

class ClassificationMetricsCalculator:
    def __init__(self):
        self.N = None
        self.true_labels = None
        self.pred_labels = None

    def _get_positive_integer(self, prompt):
        """Get valid positive integer input"""
        while True:
            try:
                value = int(input(prompt))
                if value > 0:
                    return value
                print("Must be positive. Try again.")
            except ValueError:
                print("Invalid integer. Try again.")

    def _get_binary_input(self, prompt):
        """Get valid binary (0/1) input"""
        while True:
            try:
                value = int(input(prompt))
                if value in {0, 1}:
                    return value
                print("Must be 0 or 1. Try again.")
            except ValueError:
                print("Invalid input. Must be integer 0 or 1.")

    def get_inputs(self):
        """Collect all required inputs from user"""
        self.N = self._get_positive_integer("Enter N (positive integer): ")
        
        # Pre-allocate NumPy arrays
        self.true_labels = np.empty(self.N, dtype=int)
        self.pred_labels = np.empty(self.N, dtype=int)
        
        # Fill arrays directly without append
        for i in range(self.N):
            x = self._get_binary_input(f"Enter X (true class) for point {i+1}: ")
            y = self._get_binary_input(f"Enter Y (predicted class) for point {i+1}: ")
            self.true_labels[i] = x
            self.pred_labels[i] = y

    def calculate_metrics(self):
        """Calculate and return precision and recall"""
        try:
            precision = precision_score(self.true_labels, self.pred_labels, zero_division=0)
            recall = recall_score(self.true_labels, self.pred_labels, zero_division=0)
            return precision, recall
        except Exception as e:
            print(f"Error calculating metrics: {str(e)}")
            return None, None

    def execute(self):
        """Main execution flow"""
        self.get_inputs()
        precision, recall = self.calculate_metrics()
        
        print("\nResults:")
        print(f"Precision: {precision:.4f}")
        print(f"Recall: {recall:.4f}")

if __name__ == "__main__":
    calculator = ClassificationMetricsCalculator()
    calculator.execute()