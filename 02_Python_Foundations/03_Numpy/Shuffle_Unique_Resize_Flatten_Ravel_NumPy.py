import numpy as np

print("Shuffle")
arr = np.array([1, 2, 3, 4, 5, 6, 7])
np.random.shuffle(arr)
print(arr)
print("Shuffle don't have return type , it just return the original variable ")

print("Unique")
new_arr = np.array([1, 2, 3, 4, 5, 4, 3, 2])
x = np.unique(new_arr, return_index=True, return_counts=True)
# return_index= True is print the index value of unique element
# return_counters =True it print the counter of it
print(x)
print("unique function print unique element that come once in array ")
