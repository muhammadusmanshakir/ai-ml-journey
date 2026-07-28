import numpy as np
arr=np.array([
    [12,45,78],
    [90,23,56]
])

print("Array:")
print(arr)
print("\nOverall maximum:")
print(np.max(arr))
print("\nOverall minimun:")
print(np.min(arr))
print("\nColumn Maximum:")
print(np.max(arr,axis=0))
print("\nRow Maximum:")
print(np.max(arr,axis=1))
print("\nColumn Minimum:")
print(np.min(arr,axis=0))
print("\nRow Minimum:")
print(np.min(arr,axis=1))

