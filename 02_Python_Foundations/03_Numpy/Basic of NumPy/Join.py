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

print("this is how the marge is work")
print("Another way to merge it : stack function")

x1 = np.array([[1, 2, 3, 4],
               [5, 6, 7, 8]])

y1 = np.array([[9, 8, 7, 6],
               [5, 4, 3, 2]])

# stack (adds a new dimension)
ns = np.stack((x1, y1))
print("stack:\n", ns)

# vertical stack (row-wise)
v = np.vstack((x1, y1))
print("vstack:\n", v)

# horizontal stack (column-wise)
h = np.hstack((x1, y1))
print("hstack:\n", h)

# depth stack (adds third dimension)
d = np.dstack((x1, y1))
print("dstack:\n", d)
