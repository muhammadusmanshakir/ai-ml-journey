import numpy as np
numbers=np.array([12,25,8,41,50,3,99])
print("Original Array:")
print(numbers)
print("Numbers greater than 20:")
print(numbers[numbers>20])
print("\nEven Numbers:")
print(numbers[numbers%2==0])

