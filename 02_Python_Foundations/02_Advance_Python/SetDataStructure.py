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
