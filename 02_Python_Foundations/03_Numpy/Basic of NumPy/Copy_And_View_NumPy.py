import numpy as np

x = np.array([1, 2, 3, 4])
co = x.copy()
print(f"Print the actual variable", x)
print(f"Print the copy variable", co)
print(".copy() in NumPy creates a new array with its own memory,"
      " independent of the original array.")
vi = x.view()
print(vi)
print(".view() in NumPy creates a new array object"
      " that shares the same data as the original array.")
print(" If i change data in main  variable copy will not change but view can change ")
