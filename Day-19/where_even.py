import numpy as np
arr=np.array([11,22,33,44,55,66])
print("Array:")
print(arr)

print("\nIndexes of even numbers:")
print(np.where(arr%2==0))
