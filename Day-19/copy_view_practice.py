import numpy as np
arr=np.array([1,2,3,4])
copy_arr=arr.copy()
view_arr=arr.view()
copy_arr[1]=200
view_arr[2]=300
print("Original Array:")
print(arr)
print()
print("Copied Array:")
print(copy_arr)
print()
print("View Array:")
print(view_arr)
