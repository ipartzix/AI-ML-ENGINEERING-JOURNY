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

print("3D array Indexing ")
z = np.array([[[1, 2, 3], [55, 66, 8], [12, 4, 77]]])
print(z.ndim)
print(z)
print(z[0, 1, 2])

print("SLICING")
s = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# slicing format → start : stop : step (index-based)

print("2 to 5:", s[1:5])  # index 1 to 4
print("2 to ending:", s[1:])  # index 1 to end
