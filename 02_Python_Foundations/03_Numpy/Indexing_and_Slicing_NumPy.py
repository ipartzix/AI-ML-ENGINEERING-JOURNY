print("INDEXING")
import numpy as np

print("1D array Indexing ")
x = np.array([1, 7, 56, 77, 54])
print(x.ndim)
print(x[1])
print(x[-4])

print("2D array Indexing ")
y = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])
print(y.ndim)
print(y[0, 2])
print(y[0, -1])
