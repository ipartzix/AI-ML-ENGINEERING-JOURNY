class Customer:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender



def greet(customer):
    if customer.gender == "Male":
        print("Hello", customer.name, "sir")

    else:
        print("Hello", customer.name, "ma'am")


cust = Customer("Partha", "Male")
print(cust.name)

greet(cust)
# it can be mutable


class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def introduction(self):
        print(f"I am {self.__name}  my age is {self.__age}")


S1 = Student("Partha", 21)
S2 = Student("Arjun", 22)
S3 = Student("Ram", 23)
S4 = Student("Krishna", 24)

studentList = [S1, S2, S3, S4]
for i in studentList:
    i.introduction()
