class MemberID:  # parent class


    def __init__(self):
        self.__username = "ipartzix"
        self.__password = "1234"  # password and username both are use as string


#_____________Authentication section________________

    def menu(self):
        UserID = int(input("""Did you have already Account ?\n
        1. YES
        2. NO \n"""))
        if UserID == 1:
            self.loginAcc()
            return True

        elif UserID == 2:
            self.createAcc()
            return True

        else:
            print("Wrong entry!!!!!!")
            return False

    # _______________Create Account section________________

    def createAcc(self):
        print("--------Create account---------")
        self.__username = input("Enter your Username :-")
        self.__password = input("Enter your Password :-")
        print(" Account Created successful")
        self.loginAcc()

    # ____________________Login Section____________________

    def loginAcc(self):
        print("---------Login account----------")
        try_username = input("Enter your Username :-")
        try_password = input("Enter your Password :-")

        # __________Logical AND, comparing strings_____________

        if self.__username == try_username and self.__password == try_password:
            print("login Successful")
            return True

        else:
            print("Login Failed! Incorrect username or password.")
            return False


# ____________Add Additional user Information_____________


class UserData(MemberID):  # Child class

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


user = MemberID()
user.menu()

s = UserData()
s.completeProfile()
s.showProfile()
