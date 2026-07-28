import numpy as np
arr=np.array([
    [10,20,30],
    [40,50,60]
])

print("Array:")
print(arr)
print("\nOverall mean:")
print(np.mean(arr))
print("\nColumn mean:")
print(np.mean(arr,axis=0))
print("\nRow mean:")
print(np.mean(arr,axis=1))

