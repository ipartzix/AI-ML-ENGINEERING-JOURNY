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

# Q. find the 2nd greatest element with index print

print("2nd greatest element with index ")  # Display purpose message

lis = [12, 33, 44, 55, 66, 1, 4, 6, 99, 32]  # Input list

firstLargest = float('-inf')  # Store the largest value (initialized to -infinity)
secondLargest = float('-inf')  # Store the second largest value

first_index = -1  # Index of the largest element
second_index = -1  # Index of the second largest element

for i in range(len(lis)):  # Traverse the list using index
    if lis[i] > firstLargest:  # If current element is greater than largest
        secondLargest = firstLargest  # Previous largest becomes second largest
        second_index = first_index  # Save index of previous largest

        firstLargest = lis[i]  # Update largest value
        first_index = i  # Update index of largest value

    elif lis[i] > secondLargest and lis[i] != firstLargest:
        # If current element is between largest and second largest
        secondLargest = lis[i]  # Update second largest value
        second_index = i  # Update index of second largest

print(f"first largest element is : {firstLargest} and its index is : {first_index}")  # Print largest
print(f"second largest element is : {secondLargest} and its index is : {second_index}")  # Print second largest

# check if list is sorted or not (ascending order)

a = [12, 13, 14, 15, 16]

for i in range(len(a) - 1):  # loop till second last element
    if a[i] > a[i + 1]:  # violation of sorted order
        print("list is not sorted")
        break
else:
    print("list is sorted")

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
