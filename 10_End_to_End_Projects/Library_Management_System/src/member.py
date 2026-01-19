class MemberID:
    def __init__(self):
        self.__username = "ipartzix"
        self.__password = "1234"  # password and username both are use as string



    def menu(self, ):
        UserID = int(input("""Did you have already Account ?\n
        Enter 1 for YES
        Enter 2 for NO\n"""))
        if UserID == 1:
            self.loginAcc()
        elif UserID == 2:
            self.createAcc()
        else:
            print("Wrong entry!!!!!!")

    # _____________________Create Account section____________

    def createAcc(self):
        print("create acc")
        self.__username = input("Enter your Username :-")
        self.__password = input("Enter your Password :-")
        print(" Account Created successful")
        self.loginAcc()

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


# ___________Add Additional user Information_____________


class UserData(MemberID):
    def __init__(self):
        super().__init__()  # initialize MemberID
        self.__name = None
        self.__age = None
        self.__gender = None
        self.__phone = None

    # ----- setup full profile -----

    def completeProfile(self):
        print("-----Complete Your Profile-----")
        self.__name = input("Name is :-")
        self.__age = input("Age is:-")
        self.__gender = input("Gender is:-")
        self.__phone = input("Phone is:-")
        print("Successfully profile created ")

    # ----- Show full profile -----

    def showProfile(self):
        print("\n----- User Profile -----")
        print(f"Name   : {self.__name}")
        print(f"Age    : {self.__age}")
        print(f"Gender : {self.__gender}")
        print(f"Phone  : {self.__phone}")


user = UserData()

if user.menu():  # login or signup success
    user.completeProfile()
