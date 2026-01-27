import numpy as np

print(" join of 1D array ")
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([9, 8, 7, 6, 5, 4, 3, 2, 1])

n = np.concatenate((x, y))
print(n)

print(" join of 2D array ")
x1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8, ]])
y1 = np.array([[9, 8, 7, 6], [5, 4, 3, 2, ]])

n2 = np.concatenate((x1, y1), axis=1)
print("1 axis :\n", n2)
n3 = np.concatenate((x1, y1), axis=0)
print("0 axis :\n", n3)
