import numpy as np

x = np.array([1, 2, 3, 4])
co = x.copy()
print(f"Print the actual variable", x)
print(f"Print the copy variable", co)
print(".copy() in NumPy creates a new array with its own memory,"
      " independent of the original array.")
