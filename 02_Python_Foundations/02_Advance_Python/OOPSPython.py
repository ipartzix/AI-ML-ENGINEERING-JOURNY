# class Factory:
#     a = 12  # class attribute
#
#     def __init__(self):
#         print("this is an initialized statement")
#
#     def hello(self):  # instance method
#         print("hello how are you")
#
#
# obj = Factory()  # calls __init__
# obj.hello()  # calls method
# print(obj.a)  # calls class attribute

"""
      The core concept of oops are
      1. Object
      2. Class
      3. Abstraction
      4. Polymorphism
      5. Ecapsulation
      6. Inheritances



*CLASS*

class is a blueprint --> (how an object is behave )
"""


class Car:  # always make it capital letter (PascalCase)
    colour = "Blue"  # data
    model = "Sports"  # data

    def calculate_avg_speed(self, km, time):  # snake_case
        avg = km / time
        print("The average speed is", avg)


my_car = Car()

# Pass the values for km and time here
my_car.calculate_avg_speed(120, 2)
