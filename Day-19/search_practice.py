import numpy as np

numbers = np.array([5, 10, 15, 20, 25])

print("Numbers:")
print(numbers)

print("\nIndex of 15:")
print(np.where(numbers == 15))

print("\nInsert 18 at:")
print(np.searchsorted(numbers, 18))

