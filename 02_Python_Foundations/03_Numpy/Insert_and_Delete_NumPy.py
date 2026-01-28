import numpy as np

print("1D array ")
ver = np.array([1, 2, 3, 4, 5, 61, 2, 3, 4, 5])
print(ver)
v = np.insert(ver, (2, 4), 12)  # variable name  , index position , value -----> this is for insertion
print(v)  # it only takes integer value not float value
m = np.append(ver, (1, 2, 55))  # append can also do sae of insertion, but it's done at the last position
print(m)
print("2D array ")
ver2 = np.array([[1, 3, 55, 67], [55, 7, 86, 5]])
print(ver2)
print()
# Insert a new row at index 2
# Row must have 4 elements

i = np.insert(ver2, 2, [99, 10], axis=1)
print(i)
print()
v1 = np.append(ver2, [[22, 44, 33, 3]], axis=0)
print(v1)
