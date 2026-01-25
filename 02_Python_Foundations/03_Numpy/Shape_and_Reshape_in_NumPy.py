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

print("RESHAPE")
var2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
mx = var2.reshape(3, 3)  # 1st is number of rows and 2nd is number of column
print(mx)

print()
one = mx.reshape(-1)
print(one)
print(one.ndim)
