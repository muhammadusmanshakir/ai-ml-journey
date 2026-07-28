import numpy as np
arr=np.array([
    [10,20],
    [30,40]
    ])
print("Array:")
print(arr)
print("\nIndex and value:")
for index,value in np.ndenumerate(arr):
    print(index,":",value)

    