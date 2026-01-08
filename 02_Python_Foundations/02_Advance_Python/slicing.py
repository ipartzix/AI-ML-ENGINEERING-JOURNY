# sequence[start:stop:step]
# Initialize list
lst = [50, 70, 30, 20, 90, 10, 50]
# Slice from index 1 to 5
print(lst[1:5]) # Output: [70, 30, 20, 90]
# Slice with a step of 2
print(lst[::2]) # Output: [50, 30, 90, 50]
# Slice with negative indexing
print(lst[-4:-1]) # Output: [20, 90, 10]
