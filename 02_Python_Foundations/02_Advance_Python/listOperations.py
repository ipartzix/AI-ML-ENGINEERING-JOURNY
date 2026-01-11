print("Solve some questions on lists")

# Q. print all negative and positive element on list
default_list = [1, -2, 3, -4, 5, 6, -7, -8, 9, -10]
print("positive elements are :-")
for i in default_list:
    if i >= 0:
        print(i)
print("negative elements are :-")
for i in default_list:
    if i < 0:
        print(i)

print("Thank you ")

# Q. Mean of list element

summ = 0
for i in default_list:
    summ += i
print(f"sum is : {summ}")

mean = summ / len(default_list)
print(f"mean is : {mean}")

# Q. find greatest element from list
print("Greatest Element")

le = [22, 4, 5, 66, 88, 23, 76]

largest = le[0]
index = 0
for i in range(len(le)):
    if le[i] > largest:
        largest = le[i]
        index = i

print(f"largest element is : {largest} and its index is : {index}")
