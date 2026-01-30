import numpy as np

var_1 = np.array([1, 2, 3])
print(var_1.shape)
var_2 = np.array([[1], [2], [3]])
print(var_2.shape)
print(var_1 + var_2)

print("____________________________")
x = np.array([[1], [2]])
# (2, 1) 2 number of array with 1 element

print(x.shape)
y = np.array([[1, 2, 3], [1, 2, 3]])
# (2, 3) 2 number of array with 3 element
print(y.shape)
print(x + y)

print("""
**Broadcasting in NumPy** is a mechanism that allows NumPy to perform element-wise operations on arrays of different shapes without explicitly copying data.

**Key idea:**
Smaller arrays are automatically “stretched” to match the shape of larger arrays during arithmetic operations, as long as certain rules are satisfied.

**Broadcasting rules:**

1. If arrays differ in number of dimensions, the shape of the smaller array is padded with ones on the left.
2. Dimensions are compatible if they are equal or one of them is 1.
3. If dimensions are incompatible, NumPy raises a `ValueError`.

**Benefits:**

* Avoids unnecessary memory usage.
* Makes code concise and efficient.
* Enables vectorized operations.

**Example:**
Adding a 1D array to each row of a 2D array works through broadcasting, where the 1D array is reused across rows.

Broadcasting is fundamental for high-performance numerical computation in NumPy.


""")
