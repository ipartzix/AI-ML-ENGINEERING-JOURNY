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
