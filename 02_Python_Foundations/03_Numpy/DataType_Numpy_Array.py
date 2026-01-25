# Integer Types
# | Type   | Description             |
# | -------|-------------------------|
# | int8   | 8-bit integer           |
# | int16  | 16-bit integer          |
# | int32  | 32-bit integer          |
# | int64  | 64-bit integer          |
# | uint8  | 8-bit unsigned integer  |
# | uint16 | 16-bit unsigned integer |
# | uint32 | 32-bit unsigned integer |
# | uint64 | 64-bit unsigned integer |
# NumPy Array Data Types (dtype)

# Integer types:
# int8, int16, int32, int64
# uint8, uint16, uint32, uint64

# Floating-point types:
# float16, float32, float64

# Complex number types:
# complex64, complex128

# Boolean type:
# bool_

# String types:
# U  (Unicode string)
# S  (Byte string)

# Object type:
# object_

# Date and time types:
# datetime64
# timedelta64
import numpy as np

print("Data type")
var = np.array([1, 2, 3, 4])
print("Data type :", var.dtype)

var2 = np.array([1.4, 5.6, 5.0, 7.1])
print("Data type :", var2.dtype)

var3 = np.array(["p", "3", "oo"])
print("Data type :", var3.dtype)

var4 = np.array(["p", "3", "oo", 5, 9])
print("Data type :", var4.dtype)

print("_________NumPy data type conversion_________")
x = np.array([1, 3, 4, 5, 67], dtype=np.int8)
print(x)
print("data type: ", x.dtype)
# At first, it becomes int64 now it int8 because we do type conversion
# for doing type conversion  do ----> dtype =np.targeted datatype ( dtype=np.int8 )

print("_________shortcut NumPy data type conversion_________")
x1 = np.array([1, 3, 4, 5, 67], dtype="f")
print(x1)
print("data type: ", x1.dtype)
# This is the shortcut method to convert one datatype to another data type

print("_________NumPy data type conversion function _________")
print("int -----> float")
x2 = np.array([1, 3, 4, 5, 67])
new = np.float32(x2)
print(x2)
print("data type: ", x2.dtype)
print(new)
print("data type: ", new.dtype)
print()

print("float -----> int")
new_int = np.int32(new)
print(new)
print("data type: ", new.dtype)
print(new_int)
print("data type: ", new_int.dtype)
