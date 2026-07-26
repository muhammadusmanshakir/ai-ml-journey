import numpy as np
arr=np.array([100,200,300,400,500,600])

print("Original Array:")
print(arr)

new_arr1=arr.reshape(2,3)
print("\nReshape to (2,3)")
print(new_arr1)

new_arr2=arr.reshape(3,2)
print("\nReshape to (3,2):")
print(new_arr2)
