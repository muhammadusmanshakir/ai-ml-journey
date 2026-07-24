import numpy as np
numbers=np.array([
    [100,200,300],
    [400,500,600],
    [700,800,900]
])

print("First Row:")
print(numbers[0])
print("Last Row:")
print(numbers[2])
print("First Columcn:")
print(numbers[:,0])
print("Last column:")
print(numbers[:,2])
print("First two rows:")
print(numbers[:2])
print("Last two columns:")
print(numbers[:,1:])
