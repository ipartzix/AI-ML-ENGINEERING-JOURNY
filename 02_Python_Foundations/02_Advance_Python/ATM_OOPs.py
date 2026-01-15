# It is a full flared ATM machine system design in oops code structure
# to understand the concept of Object-Oriented-Programming
class Atm:
    def __init__(self):  # __init__ is a constructor // Constructor is a special method  ,< self > always run itself
        self.pin = ""
        self.balance = 0

        self.menu()

    def menu(self):
        pass
