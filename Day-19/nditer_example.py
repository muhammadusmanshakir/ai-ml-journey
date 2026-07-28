import numpy as np
arr=np.array([
    [10,20,30],
    [40,50,60]
])

print("Array:")
print(arr)

print("Using nditer():")
for item in np.nditer(arr):
    print(item)
