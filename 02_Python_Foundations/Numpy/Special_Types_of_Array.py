import numpy as np

print("Special type of Array")
print("_________________________________________________________________________")
print("Array filled with zero")
ar_zero = np.zeros(4)  # zeros is a function which help to create Array filled with zero
ar_zero1 = np.zeros((4, 2))
print(ar_zero)
print("\n4,2 array")
print(ar_zero1)

print("__________________________________________________________________________")
print("Array filled with 1")
arr_one = np.ones(3)  # ones is the keyword to do this kind of operation
print(arr_one)

print("__________________________________________________________________________")
print("Empty array ")
ar_empty = np.empty(4)  # .empty is the keyword to do that kind of operation
print(ar_empty)

print("___________________________________________________________________________")
print("An Array with a range element ")
arr_range = np.arange(4)  # to create a continuous order of number like 0 1 2 3 4 .... we use this arange function
print(arr_range)
