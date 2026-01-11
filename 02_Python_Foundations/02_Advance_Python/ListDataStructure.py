fruits = ["apple", "banana", "cherry"]
number =[11,55,3434, 55]
print(number[3])
print(fruits[2])
print(number[0::1])

# 1st way of list Traversal using index
for i in range(len(number)):
    print(number[i])

# 2nd way of list Traversal Directly on value
for i in number:
    print(i)

for i in fruits:
    print(i)

# Method

print("append")
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l.append(12)
print(l)
l.append(33)
print(l)
# append always add element at the last


print("Insert")
l.insert(1, 12)
print(l)
# .insert works on index value it add an element at the targeted index just add an new element but do not replace it previous on this index it just shift it (i+1 ; i= targeted index value )

print("Extend")
m = [22, 33, 44, 55]
l.extend(m)
print(l)

# .extend use to add anot her list and marge it in the current list


print("remove")
l.remove(1)
print(l)

# remove the element by value inputed
