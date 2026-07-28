import numpy as np
arr=np.array([
    [100,200,300],
    [400,500,600]
])

print("Using nditer():")
for item in np.nditer(arr):
    print(item)

print("Using ndenumerate():")
for index,value in np.ndenumerate(arr):
    print(index,":",value)

