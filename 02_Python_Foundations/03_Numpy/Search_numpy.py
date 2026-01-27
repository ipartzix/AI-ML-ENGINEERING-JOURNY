# =====================================================================
# NumPy Notes: Search, Sort, SearchSorted, and Filtering
# =====================================================================

# 1. Search / Where
# -----------------
# The np.where() function is used to find indices where a condition is True.

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Find indices where element is greater than 25
indices = np.where(arr > 25)
print(indices)  # Output: (array([2, 3, 4]),)

# Using np.where() to replace values
# Replace values > 25 with 99
new_arr = np.where(arr > 25, 99, arr)
print(new_arr)  # Output: [10 20 99 99 99]

# ---------------------------------------------------------------------
# 2. Sort
# --------
# np.sort() returns a sorted copy of the array (does not change original array)
# arr.sort() sorts the array in-place

arr_unsorted = np.array([50, 10, 30, 20, 40])

# Using np.sort()
sorted_arr = np.sort(arr_unsorted)
print(sorted_arr)  # Output: [10 20 30 40 50]

# Sorting in-place
arr_unsorted.sort()
print(arr_unsorted)  # Output: [10 20 30 40 50]

# Sorting along axis (for 2D arrays)
arr_2d = np.array([[3, 1, 2], [6, 4, 5]])
sorted_2d = np.sort(arr_2d, axis=1)  # sort along rows
print(sorted_2d)  # Output: [[1 2 3] [4 5 6]]

# ---------------------------------------------------------------------
# 3. SearchSorted
# ----------------
# np.searchsorted() finds the index where an element should be inserted to maintain order.

arr_sorted = np.array([10, 20, 30, 40, 50])

# Find insertion index for 35
index = np.searchsorted(arr_sorted, 35)
print(index)  # Output: 3 (35 should go at index 3 to keep array sorted)

# Multiple values
indices = np.searchsorted(arr_sorted, [5, 25, 60])
print(indices)  # Output: [0 2 5]

# Side option ('left' or 'right') for duplicate elements
arr_dup = np.array([10, 20, 20, 30])
print(np.searchsorted(arr_dup, 20, side='left'))  # Output: 1
print(np.searchsorted(arr_dup, 20, side='right'))  # Output: 3

# ---------------------------------------------------------------------
# 4. Filtering / Boolean Indexing
# --------------------------------
# Boolean indexing is used to filter elements based on a condition.

arr = np.array([10, 20, 30, 40, 50])

# Filter elements greater than 25
filtered_arr = arr[arr > 25]
print(filtered_arr)  # Output: [30 40 50]

# Filter using multiple conditions
filtered_arr2 = arr[(arr > 15) & (arr < 45)]
print(filtered_arr2)  # Output: [20 30 40]

# Using np.isin() for filtering specific values
arr = np.array([1, 2, 3, 4, 5])
filtered_arr3 = arr[np.isin(arr, [2, 4])]
print(filtered_arr3)  # Output: [2 4]

# ---------------------------------------------------------------------
# Summary:
# 1. np.where(): Returns indices where condition is True, also can replace values.
# 2. np.sort(): Sorts array, can sort along axes, returns new array or in-place.
# 3. np.searchsorted(): Finds insertion index to maintain order in sorted array.
# 4. Boolean Indexing / Filtering: Extract elements using conditions or np.isin().
# =====================================================================
