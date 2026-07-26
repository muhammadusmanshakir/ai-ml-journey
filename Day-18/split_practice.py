import numpy as np
arr=np.array([100,200,300,400])
print("Original Array:")
print(arr)
parts=np.split(arr,2)
print("\nFirst part:")
print(parts[0])
print("\nSecond part:")
print(parts[1])
