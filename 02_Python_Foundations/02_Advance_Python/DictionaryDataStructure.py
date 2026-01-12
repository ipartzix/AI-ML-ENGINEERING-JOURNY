d = {1: "Ram", 2: "Krishna", 3: " Radha krishna"}
print(d[3])

d.update({44: "2345"})  # updating

print(d)

d[50] = 888  # creating
print(d)

del d[44]
print(d)

des = {10: 33, 20: 44, 30: 554, 40: 68794, 50: 7547}
for i in des:
    print(des[i])
for key, value in des.items():
    print(F"{key} :{value}")

# ============================================
# SHALLOW COPY vs DEEP COPY IN PYTHON DICTIONARY
# ============================================

import copy  # import copy module for deep copy

# ------------------------------------------------
# ORIGINAL DICTIONARY
# ------------------------------------------------
original = {
    "name": "Partha",
    "marks": [85, 90, 95],  # nested mutable object (list)
    "details": {"age": 21}  # nested mutable object (dict)
}

# ------------------------------------------------
# SHALLOW COPY
# ------------------------------------------------
# Creates a new dictionary object
# BUT nested objects (list, dict) are shared
shallow_copy = original.copy()

# Modifying nested data in shallow copy
shallow_copy["marks"].append(100)
shallow_copy["details"]["age"] = 22

# Changes reflect in BOTH dictionaries
print("Original after shallow copy change:", original)
print("Shallow copy:", shallow_copy)

# Checking memory address of nested objects
print("Same list object (shallow)?", id(original["marks"]) == id(shallow_copy["marks"]))
print("Same dict object (shallow)?", id(original["details"]) == id(shallow_copy["details"]))

print("\n--------------------------------------------\n")

# ------------------------------------------------
# DEEP COPY
# ------------------------------------------------
# Creates a new dictionary object
# AND recursively copies all nested objects
deep_copy = copy.deepcopy(original)

# Modifying nested data in deep copy
deep_copy["marks"].append(200)
deep_copy["details"]["age"] = 30

# Changes do NOT reflect in original dictionary
print("Original after deep copy change:", original)
print("Deep copy:", deep_copy)

# Checking memory address of nested objects
print("Same list object (deep)?", id(original["marks"]) == id(deep_copy["marks"]))
print("Same dict object (deep)?", id(original["details"]) == id(deep_copy["details"]))

# ------------------------------------------------
# SUMMARY (IMPORTANT NOTES)
# ------------------------------------------------
# 1. Shallow Copy:
#    - Copies only the outer dictionary
#    - Nested mutable objects are shared
#    - Changes in nested data affect original

# 2. Deep Copy:
#    - Copies outer dictionary + all nested objects
#    - No shared references
#    - Changes are fully independent

# ------------------------------------------------
# INTERVIEW ONE-LINER
# ------------------------------------------------
# Shallow copy copies references; deep copy copies objects.


print("marge two DICTIONARY")
d1 = {12: 22, 20: 35, 30: 35, 40: 554}
d2 = {1: 2, 2: 44, 3: 43, 4: 433, 5: 37}
for i in d2:
    d1[i] = d2[i]

print(d1)
