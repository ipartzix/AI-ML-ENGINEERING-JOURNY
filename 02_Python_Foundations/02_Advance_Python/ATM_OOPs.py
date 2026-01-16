# It is a full flared ATM machine system design in oops code structure
# to understand the concept of Object-Oriented-Programming
class Atm:
    def __init__(self):  # __init__ is a constructor // Constructor is a special method  ,< self > always run itself
        # self is the object that we are working right now
        # for our case we create an object name is sbi [ sbi = Atm() ]
        self.pin = ""
        self.balance = 0

        print(id(self)) 

        self.menu()

    # one method can not access with another method directly they take help of object
    # so for every method self do this job the objectb is pass through self and without self the code show error

    def menu(self): 
        user_input = input(
            """ 
                Hello , how would like to proceed ?
                1.Enter to create pin 
                2.Enter to deposit 
                3.Enter to withdraw 
                4.Enter to check balance 
                5.Enter to exit
        """)

        if user_input == "1":  # Fixed: comparing string to string
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("Bye ")

# Creating an object of the class
sbi = Atm()

def create_pin(self):
    self.pin = input("Enter pin : ")
    print("Pin created Successfully !")


def deposit(self):
    temp = input("Enter your pin : ")
    if temp == self.pin:
        amount = int(input("Enter amount : "))
        self.balance = self.balance + amount
        print("Deposit successful /nYour balance is: ", self.balance)
    else:
        print("Invalid pin !")


def withdraw(self):
    temp = int(input("Enter your pin : "))
    if temp == self.pin:
        amount = int(input("Enter amount : "))
        if amount > self.balance:
            self.balance = self.balance - amount
            print("withdraw successful /nYour balance is: ", self.balance)
        else:
            print("insufficient balance !")
    else:
        print("Invalid pin !")


def check_balance(self):
    temp = input("Enter your pin: ")
    if temp == self.pin:
        print(f"Your balance is: {self.balance}")
    else:
        print("Invalid pin!")
