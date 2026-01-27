import numpy as np

print(" join of 1D array ")
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([9, 8, 7, 6, 5, 4, 3, 2, 1])

n = np.concatenate((x, y))
print(n)
