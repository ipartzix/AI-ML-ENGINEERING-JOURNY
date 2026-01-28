import numpy as np

ver = np.array([1, 2, 3, 4, 5, 61, 2, 3, 4, 5])
print(ver)
v = np.insert(ver, (2, 4), 12)  # variable name  , index position , value -----> this is for insertion
print(v)  # it only takes integer value not float value
m = np.append(ver, (1, 2, 55))  # append can also do sae of insertion, but it's done at the last position
print(m)
