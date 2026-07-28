import numpy as np
arr=np.array([10,20,30,40,50])
view_arr=arr.view()
view_arr[0]=100
print("Original Array:")
print(arr)
print()
print("View Array:")
print(view_arr)

