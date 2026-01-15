# It is a full flared ATM machine system design in oops code structure
# to understand the concept of Object-Oriented-Programming
class Atm:
    def __init__(self):  # __init__ is a constructor // Constructor is a special method  ,< self > always run itself
        self.pin = ""
        self.balance = 0

        self.menu()

    def menu(self):
        user_input = input(
            """ 
                Hello , how would like to proceed ?
                1.Enter 1 to create pin 
                2.Enter 2 to deposit 
                3.Enter 3 to withdraw 
                4.Enter 4 to check balance 
                5.Enter 5 to exit
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

