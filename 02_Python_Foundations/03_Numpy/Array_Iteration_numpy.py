import numpy as np

x = np.array([11, 33, 44, 66, 88, 77])
for i in x:
    print(i)

v = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
for j in v:
    print(j)
print("Individual data iteration ")
for k in v:
    for l in k:
        print(l)

d = np.array([[[1, 2, 3], [1, 2, 3], [1, 2, 3]]])
print(d)
for i in d:
    for j in i:
        for k in j:
            print(k)
print("Array  data iteration by function  ")
cd = np.array([[[1, 2, 3], [1, 2, 3], [1, 2, 3]]])

for i in np.nditer(cd):  # .nditer is a function to do the iteration
    print(i)
print()

# for i in np.nditer(cd,flags=['buffered '],op_dtypes=["s"]):
#     print(i)
for i in np.nditer(cd, flags=['buffered'], op_dtypes=['S']):
    print(i)
