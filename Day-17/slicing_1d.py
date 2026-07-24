import numpy as np

numbers = np.array([10, 20, 30, 40, 50, 60])

print("Original Array:")
print(numbers)

print("\nFirst three elements:")
print(numbers[0:3])

print("\nFrom index 2 to 4:")
print(numbers[2:5])

print("\nFrom index 3 to end:")
print(numbers[3:])

print("\nFrom beginning to index 4:")
print(numbers[:5])

print("\nEvery second element:")
print(numbers[::2])