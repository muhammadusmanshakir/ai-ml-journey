import numpy as np

numbers = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print(numbers)

print("\nFirst Layer, First Row, First Column :", numbers[0, 0, 0])
print("First Layer, Second Row, Second Column:", numbers[0, 1, 1])
print("Second Layer, First Row, Second Column:", numbers[1, 0, 1])
print("Second Layer, Second Row, First Column:", numbers[1, 1, 0])
