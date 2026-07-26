import numpy as np

arr = np.array([
    [100,200],
    [300,400]
])

print("Original Array:")
print(arr)

ravel_arr = arr.ravel()

print("\nRavel Array:")
print(ravel_arr)