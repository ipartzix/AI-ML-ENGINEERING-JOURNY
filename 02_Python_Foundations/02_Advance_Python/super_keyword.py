class Phone:
    def __init__(self, price, brand, camera):
        print("Inside the phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")


class SmartPhone(Phone):
    def buy(self):
        print("Buying a Smartphone !")
        super().buy()  # super is used to access parent-class methods or constructors from a child class. It prevents code duplication and preserves inheritance behavior-  | this keyword cannot work outside the child class


"""

"""

s = SmartPhone(10000, "apple", 48)
s.buy()
