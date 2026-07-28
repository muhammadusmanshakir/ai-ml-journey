import numpy as np
arr=np.array([
    [10,20,30],
    [40,50,60]
])
print("Array:")
print(arr)
print("\nElemnts:")

for row in arr:
    for item in row:
        print(item)

        