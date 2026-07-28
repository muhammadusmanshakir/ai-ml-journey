import numpy as np
arr=np.array([
    [10,20,30],
    [40,50,60]
])
print("Array:")
print(arr)

print("Sum of all elements:")
print(np.sum(arr))
print("\nColumn wise sum (axis=0):")
print(np.sum(arr,axis=0))

print("\nRow wise Sum:")
print(np.sum(arr,axis=1))

