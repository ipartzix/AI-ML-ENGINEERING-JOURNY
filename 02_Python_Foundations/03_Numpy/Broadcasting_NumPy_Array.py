import numpy as np

var_1 = np.array([1, 2, 3])
print(var_1.shape)
var_2 = np.array([[1], [2], [3]])
print(var_2.shape)
print(var_1 + var_2)

print("____________________________")
x = np.array([[1], [2]])
# (2, 1) 2 number of array with 1 element

print(x.shape)
y = np.array([[1, 2, 3], [1, 2, 3]])
# (2, 3) 2 number of array with 3 element
print(y.shape)
print(x + y)
