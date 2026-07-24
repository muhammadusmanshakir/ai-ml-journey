import numpy as np

numbers = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Original Array:")
print(numbers)

print("\nFirst Row:")
print(numbers[0])

print("\nSecond Row:")
print(numbers[1])

print("\nFirst Column:")
print(numbers[:, 0])

print("\nSecond Column:")
print(numbers[:, 1])

print("\nLast Column:")
print(numbers[:, 2])

print("\nFirst Two Rows:")
print(numbers[:2])

print("\nLast Two Rows:")
print(numbers[1:])
