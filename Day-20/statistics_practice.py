import numpy as np

marks = np.array([
    [80,70,90],
    [60,75,85],
    [95,88,92]
])

print("Marks:")
print(marks)

print("\nColumn Sum:")
print(np.sum(marks, axis=0))

print("\nRow Sum:")
print(np.sum(marks, axis=1))

print("\nColumn Average:")
print(np.mean(marks, axis=0))

print("\nRow Average:")
print(np.mean(marks, axis=1))

