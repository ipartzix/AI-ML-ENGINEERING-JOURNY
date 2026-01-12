a = (1, 2, 3, 4, 5, 5, 6, 5, 5, 5, 5, 5, 5, 6)
print(type(a))
print(a[2])

for i in range(len(a)):
    print(a[i])

index = a.index(5)
print("Index printing")
print(index)
print("count of occurrences ")
count = a.count(5)
print(count)

print("Tuple unpacking ")
a, b, c, d, e, f, g, h = (1, 2, 3, 4, 5, 6, 7, 8)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)

j = (86)  # in tuple single value are always unpack
print(j)
print(type(j))
# <class 'int'>

m = (33,)  # ( ,) coma will help to blocking unpacking the tuple
print(type(m))
# <class 'tuple'>
