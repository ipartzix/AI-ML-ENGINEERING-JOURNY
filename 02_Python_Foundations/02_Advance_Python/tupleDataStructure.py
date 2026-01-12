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
