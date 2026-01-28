import numpy as np

print("Transpose ")
var = np.matrix([[1, 2, 3], [4, 5, 6]])
print(var)
print()
print(np.transpose(var))
print()
print(var.T)  # T is a shortcut of this function transpose
print("Swapaxes")
var2 = np.matrix([[1, 2], [3, 4]])
print(var2)
print()
print(np.swapaxes(var2, 0, 1))
