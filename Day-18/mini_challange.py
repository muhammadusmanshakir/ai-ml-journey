import numpy as np

arr = np.array([
    [1,2],
    [3,4]
])

ravel_arr = arr.ravel()

ravel_arr[0] = 100

print("Ravel Array:")
print(ravel_arr)

print("\nOriginal Array:")
print(arr)