class Customer:
    def __init__(self, name):
        self.name = name


def greet(customer):
    print("Hello", customer.name)


cust = Customer("Partha")
print(cust.name)

greet(cust)
