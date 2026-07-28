import numpy as np

numbers = np.array([44, 12, 90, 3, 67, 25])

print("Original:")
print(numbers)

print("\nSorted:")
print(np.sort(numbers))

print("\nLargest Number:")
print(np.sort(numbers)[-1])

print("\nSmallest Number:")
print(np.sort(numbers)[0])
