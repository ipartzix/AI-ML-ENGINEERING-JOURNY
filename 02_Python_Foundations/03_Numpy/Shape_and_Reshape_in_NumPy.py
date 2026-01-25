import numpy as np

print("SHAPE")
var = np.array([[1, 2], [2, 1]])
print(var)
print()
print(var.shape)  # .shape is a function to see the dimension of it like 2*2 , 3*3

var1 = np.array([1, 2, 3, 4, 5, 6], ndmin=3)
print(var1)
print(var1.ndim)
print()
print(var1.shape)
