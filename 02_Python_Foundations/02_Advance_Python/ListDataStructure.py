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
