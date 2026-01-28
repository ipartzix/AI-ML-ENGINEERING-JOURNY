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
