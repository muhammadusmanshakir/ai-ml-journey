import numpy as np
arr1=np.array([100,200])
arr2=np.array([300,400])
print("Array 1:")
print(arr1)
print("\nArray 2:")
print(arr2)

result=np.concatenate((arr1,arr2))
print("After Concatenation")
print(result)

result1=np.hstack((arr1,arr2))
print("After H stack:")
print(result1)

result2=np.vstack((arr1,arr2))
print("After v stack:")
print(result2)

