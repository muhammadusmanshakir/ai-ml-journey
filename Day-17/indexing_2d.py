import numpy as np

numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(numbers)

print("\nFirst Row, First Column :", numbers[0, 0])
print("First Row, Third Column :", numbers[0, 2])
print("Second Row, First Column:", numbers[1, 0])
print("Second Row, Second Column:", numbers[1, 1])
print("Second Row, Third Column :", numbers[1, 2])

