a = {1, 2, 3, 4, 5, 6, 2, 1}
print(type(a))
print(a)

a.remove(2)
print(a)

a.pop()
print(a)

print("clear method ")
a.clear()
print(a)

b = {1, 2, 3, 4, 5}
d = {4, 5, 6, 7, 8}

s = b.union(d)  # b|d
print(f" the union is {s}")

t = b.intersection(d)  # b & d
print(f" the intersection is {t}")

y = b.difference(d)  # b - d
print(f" the difference is {y}")

sd = b.symmetric_difference(d)  # b ^ d
print(f" the symmetric_difference is {sd}")

print(" frequency count of each element in list ")
demoList = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6]

dic = {}

count = 0
for i in demoList:
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1

print(dic)

# ------------------------------------------------
# MERGE TWO DICTIONARIES AND ADD VALUES FOR SAME KEYS
# ------------------------------------------------

dd1 = {10: 100, 20: 200, 40: 400}
dd2 = {40: 400, 50: 500, 60: 600}

# Create a copy of dd1 so original dd1 remains unchanged
dic = dd1.copy()

# Iterate over second dictionary
for i in dd2:
    # If key exists in dic, add values
    if i in dic:
        dic[i] += dd2[i]
    else:
        # If key does not exist, add key-value pair
        dic[i] = dd2[i]

# Print merged dictionary
print(dic)

# ------------------------------------------------
# OUTPUT:
# {10: 100, 20: 200, 40: 800, 50: 500, 60: 600}
# ------------------------------------------------

# FIXES APPLIED:
# 1. 'dic' was undefined → initialized using dd1.copy()
# 2. Used 'dic' for merging, not 'dd2'
# 3. Printed final merged dictionary instead of dd2
