class Factory:
    a = 12  # class attribute

    def __init__(self):
        print("this is an initialized statement")

    def hello(self):  # instance method
        print("hello how are you")


obj = Factory()  # calls __init__
obj.hello()  # calls method
print(obj.a)  # calls class attribute
