import numpy as np
arr=np.array([10,20,30,40])
copy_arr=arr.copy()
copy_arr[0]=100

print("Original Array:")
print(arr)
print()
print("Copied Array:")
print(copy_arr)
