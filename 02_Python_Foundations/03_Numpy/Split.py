import numpy as np

print("Splitting breaks one array into multiple")
x = np.array([1, 2, 3, 4, 5, 6])  # this is 1D array
print(x)
ar = np.array_split(x, 3)
print(ar)

print("2D array")
y = np.array([[1, 2, 3, 4], [4, 6, 9, 2]])
print(y)
a2r = np.array_split(y, 3)
print(a2r)
print("IF we want to print it with axis ")
arx = np.array_split(y, 3, axis=1)
print()
print(arx)
