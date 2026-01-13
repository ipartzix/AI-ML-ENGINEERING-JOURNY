a = int(input("enter a number : "))

try:
    b = (10 / a)
except ZeroDivisionError:
    print("u can not enter 0")
print(b)
print("done")
# exception handling with try and expect
