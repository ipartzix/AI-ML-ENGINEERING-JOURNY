class MemberID:
    def __init__(self):
        self.__username = "ipartzix"
        self.__password = "1234"

        # self.__age=""
        # self.__gender =""
        # self.__phone=""

    def menu(self, ):
        UserID = int(input("""Did you have already Account ?\n
        Enter 1 for YES
        Enter 2 for NO\n"""))
        if UserID == 1:
            print("Welcome back")
        elif UserID == 2:
            print("Create an account")
        else:
            print("Wrong entry!!!!!!")

    # _____________________Create Account section____________

    def createAcc(self):
        print("create acc")
        self.__username = input("Enter your Username :-")
        self.__password = input("Enter your Password :-")
        print(" Account Create successful")

    # ____________________Login Section______________________

    def loginAcc(self):
        print("login acc")
        try_username = input("Enter your Username :-")
        try_password = input("Enter your Password :-")

        # ___________ Logical AND, comparing strings______________

        if self.__username == try_username and self.__password == try_password:
            print("login Successful")

        else:
            print("Login Failed! Incorrect username or password.")


b = MemberID()
b.menu()
