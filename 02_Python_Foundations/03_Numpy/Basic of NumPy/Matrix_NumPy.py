# ========================= NUMPY MATRIX – COMPLETE NOTE =========================
# NOTE:
# np.matrix is a specialized 2D matrix class in NumPy.
# It is NOT recommended for new code and is considered legacy.
# NumPy officially recommends using np.ndarray instead.

import numpy as np

# ------------------------------------------------------------------------------
# 1. Creating a NumPy matrix
# ------------------------------------------------------------------------------

m1 = np.matrix([[1, 2, 3],
                [4, 5, 6]])

print(m1)
print(type(m1))  # <class 'numpy.matrix'>

# IMPORTANT:
# - np.matrix is ALWAYS 2D
# - Even a single row or column is treated as 2D

# ------------------------------------------------------------------------------
# 2. Shape and dimensions
# ------------------------------------------------------------------------------

print(m1.shape)  # (rows, columns)
print(m1.ndim)  # Always 2 for matrix

# ------------------------------------------------------------------------------
# 3. Matrix vs Array (core difference)
# ------------------------------------------------------------------------------

a1 = np.array([[1, 2],
               [3, 4]])

m2 = np.matrix([[1, 2],
                [3, 4]])

# * operator behavior
print(a1 * a1)  # Element-wise multiplication (ARRAY)
print(m2 * m2)  # Matrix multiplication (MATRIX)

# This difference causes silent logical bugs → very dangerous

# ------------------------------------------------------------------------------
# 4. Matrix multiplication operators
# ------------------------------------------------------------------------------

# Matrix multiplication using *
result1 = m2 * m2

# Matrix multiplication using dot()
result2 = np.dot(m2, m2)

# Matrix multiplication using @ (recommended modern way)
result3 = m2 @ m2

# ------------------------------------------------------------------------------
# 5. Transpose
# ------------------------------------------------------------------------------

# Transpose of matrix
print(m1.T)  # or m1.transpose()

# ------------------------------------------------------------------------------
# 6. Inverse of matrix
# ------------------------------------------------------------------------------

m3 = np.matrix([[1, 2],
                [3, 4]])

# Inverse exists only for square, non-singular matrices
inv_m3 = np.linalg.inv(m3)
print(inv_m3)

# ------------------------------------------------------------------------------
# 7. Determinant
# ------------------------------------------------------------------------------

det = np.linalg.det(m3)
print(det)

# ------------------------------------------------------------------------------
# 8. Identity matrix
# ------------------------------------------------------------------------------

# Creates identity matrix of size n x n
identity = np.identity(3)
print(identity)

# ------------------------------------------------------------------------------
# 9. Zero and One matrices
# ------------------------------------------------------------------------------

zero_mat = np.zeros((2, 3))
one_mat = np.ones((2, 3))

print(zero_mat)
print(one_mat)

# ------------------------------------------------------------------------------
# 10. Diagonal matrix
# ------------------------------------------------------------------------------

diag = np.diag([1, 2, 3])
print(diag)

# ------------------------------------------------------------------------------
# 11. Indexing and slicing
# ------------------------------------------------------------------------------

# Access element
print(m1[0, 1])  # row 0, column 1

# Access full row
print(m1[0, :])

# Access full column
print(m1[:, 1])

# ------------------------------------------------------------------------------
# 12. Matrix addition and subtraction
# ------------------------------------------------------------------------------

m4 = np.matrix([[1, 1, 1],
                [1, 1, 1]])

print(m1 + m4)
print(m1 - m4)

# ------------------------------------------------------------------------------
# 13. Broadcasting (limited support in matrix)
# ------------------------------------------------------------------------------

# Broadcasting works but is less flexible than ndarray
print(m1 + 10)

# ------------------------------------------------------------------------------
# 14. Conversion between matrix and array
# ------------------------------------------------------------------------------

# Convert matrix to ndarray
arr_from_mat = np.asarray(m1)
print(type(arr_from_mat))  # <class 'numpy.ndarray'>

# Convert ndarray to matrix
mat_from_arr = np.asmatrix(arr_from_mat)
print(type(mat_from_arr))  # <class 'numpy.matrix'>

# ------------------------------------------------------------------------------
# 15. Why np.matrix is DISCOURAGED (Very Important)
# ------------------------------------------------------------------------------

# - Always 2D (no flexibility)
# - * operator behaves differently than ndarray
# - Poor compatibility with modern NumPy APIs
# - Official NumPy documentation discourages its use
# - May be removed or unsupported in future versions

# ------------------------------------------------------------------------------
# 16. Recommended replacement (BEST PRACTICE)
# ------------------------------------------------------------------------------

# Use ndarray for everything
A = np.array([[1, 2],
              [3, 4]])

# Use @ for matrix multiplication
B = A @ A

# Use explicit functions for clarity
C = np.linalg.inv(A)
D = np.linalg.det(A)

# ------------------------------------------------------------------------------
# FINAL VERDICT (IMPORTANT FOR EXAMS & INTERVIEWS)
# ------------------------------------------------------------------------------

#  Do NOT use np.matrix in new code
#  Always use np.ndarray + @ operator
#  ndarray is the industry and research standard
# ==============================================================================
