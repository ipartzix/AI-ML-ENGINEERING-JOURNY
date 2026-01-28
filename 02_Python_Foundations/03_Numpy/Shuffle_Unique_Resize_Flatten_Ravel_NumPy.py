import numpy as np

print("Shuffle")
arr = np.array([1, 2, 3, 4, 5, 6, 7])
np.random.shuffle(arr)
print(arr)
print("Shuffle don't have return type , it just return the original variable ")

print("Unique")
new_arr = np.array([1, 2, 3, 4, 5, 4, 3, 2])
x = np.unique(new_arr, return_index=True, return_counts=True)
# np.unique() returns unique elements from the array
# return_index=True  → returns the index of the first occurrence of each unique element
# return_counts=True → returns how many times each unique element appears
print(x)
print("unique function print unique element that come once in array ")
# NOTE:
# np.unique() does NOT return elements that appear only once by default.
# It returns ALL unique elements (removes duplicates).

print("Resize")
arr2 = np.array([1, 3, 2, 4, 5, 6, 7, 23])
r = np.resize(arr2, (2, 5))  # give the targeted shape
print(r)

# flatten() and ravel() convert multi-dimensional arrays into 1D arrays
# The "order" parameter controls HOW elements are read

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("Original array:\n", arr)

# --------------------------------------------------
# order = 'C'  (Row-major order)  [DEFAULT]
# Read row by row (left to right, top to bottom)
# --------------------------------------------------

print("\nC-order flatten:", arr.flatten(order='C'))
print("C-order ravel  :", arr.ravel(order='C'))

# Output → [1 2 3 4 5 6]


# --------------------------------------------------
# order = 'F'  (Column-major order)
# Read column by column (top to bottom)
# --------------------------------------------------

print("\nF-order flatten:", arr.flatten(order='F'))
print("F-order ravel  :", arr.ravel(order='F'))

# Output → [1 4 2 5 3 6]


# --------------------------------------------------
# order = 'A'  (Automatic order)
# Uses:
#   - 'F' order if array is Fortran-contiguous
#   - 'C' order otherwise
# --------------------------------------------------

print("\nA-order flatten:", arr.flatten(order='A'))
print("A-order ravel  :", arr.ravel(order='A'))

# Output → same as C-order (because array is C-contiguous)


# --------------------------------------------------
# order = 'K'  (Keep memory order)
# Reads elements in the order they are stored in memory
# Does NOT reorder unless required
# --------------------------------------------------

print("\nK-order flatten:", arr.flatten(order='K'))
print("K-order ravel  :", arr.ravel(order='K'))

# Output → same as C-order for this array


# --------------------------------------------------
# Demonstrating difference using transposed array
# --------------------------------------------------

arr_T = arr.T  # transpose changes memory layout

print("\nTransposed array:\n", arr_T)

print("\nC-order flatten (T):", arr_T.flatten(order='C'))
print("F-order flatten (T):", arr_T.flatten(order='F'))
print("K-order flatten (T):", arr_T.flatten(order='K'))

print("\nC-order ravel (T):", arr_T.ravel(order='C'))
print("F-order ravel (T):", arr_T.ravel(order='F'))
print("K-order ravel (T):", arr_T.ravel(order='K'))
