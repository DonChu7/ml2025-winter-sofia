# -*- coding: utf-8 -*-
"""
Spyder Editor

The program asks the user for input N (positive integer) and reads it
Then the program asks the user to provide N numbers (one by one) and 
reads all of them (again, one by one)
In the end, the program asks the user for input X (integer) and 
outputs: "-1" if there were no such X among N read numbers, or the 
index (from 1 to N) of this X if the user inputed it before.
"""

while True:
    N = input("Enter a positive integer N (or type 'exit' to quit): ")
    if N.lower() == 'exit':
        print("Exiting the program...")
        break
    try:
        N = int(N)
        if N <= 0:
            print("N must be a positive integer. Please try again.")
            continue
    except ValueError:
        print("Invalid input. Please enter a positive integer or type 'exit' to quit.")
        continue

    numbers = []

    for i in range(N):
        while True:
            try:
                num = int(input(f"Enter number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    while True:
        try:
            X = int(input("Enter an integer X to search for: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    if X in numbers:
        index = numbers.index(X) + 1
        print(f"The index of {X} is: {index}")
    else:
        print("-1")

    print("\n" + "=" * 30 + "\n")