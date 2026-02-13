class MemberID:  # parent class

    # cteare a constructor to run the code(__init__)

    def __init__(self):  # Initialize the object with private credentials (Encapsulation)
        self.__username = "ipartzix"  # set a default username & password
        self.__password = "1234"  # password and username both are use as string

    # --------------- to get username and password ---------------

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    # _____________Authentication section________________

    def menu(self):
        UserID = int(input("""Did you have already Account ?\n
        1. YES
        2. NO \n"""))
        if UserID == 1:
            return self.loginAcc()  # replace the return position for fix (But menu() still blindly returns True.)

        elif UserID == 2:
            return self.createAcc()

        else:
            print("Wrong entry!!!!!!")
            return False

    # _______________Create Account section________________

    def createAcc(self):
        print("--------Create account---------")
        self.__username = input("Enter your Username :-")
        self.__password = input("Enter your Password :-")
        print(" Account Created successful")
        return True  # this return statement work as a signal that “This operation succeeded. You may continue".
        # Without this signal, Python assumes failure or unknown state.

    # ____________________Login Section____________________

    def loginAcc(self):
        print("---------Login account----------")
        try_username = input("Enter your Username :-")
        try_password = input("Enter your Password :-")
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
        self.__name = None  # create all attributes as  private and null in child class
        self.__age = None
        self.__gender = None
        self.__phone = None

    def get_name(self):
        return self.__name

    # ---------------- Authentication wrapper ----------------

    def authenticate(self):  # Call menu() to login or create account
        success = self.menu()
        if success:  # If authentication is successful

            return {
                "username": self.get_username(),
                "name": self.get_name()
            }
        # If authentication fails

        return None

    # ________ We OVERRIDE loginAcc to add the profile update logic_____

    def loginAcc(self):
        # 1. Call the parent's login logic first
        success = super().loginAcc()

        # This is for login user to ask update profile or not

        # 2. If login was successful, ask for update
        if success:
            update = input("""Would you like to update profile? 
            1 for Yes
            2 for No 
             """)
            if update == "1":
                self.updateProfile()
                self.showProfile()
            else:
                print("It's Okay")
        return success

    # This is for user who recently created account he needs to complete profile
    def createAcc(self):
        success = super().createAcc()
        if success:
            self.updateProfile()
            self.showProfile()
        return success

    # ----- setup or update full profile -----

    def updateProfile(self):
        print("-----Complete Your Profile-----")
        self.__name = input("Name is :-")
        self.__age = input("Age is:-")
        self.__gender = input("Gender is:-")
        self.__phone = input("Phone is:-")
        print("Successfully profile Updated ")

        # ----- Show full profile -----

    def showProfile(self):
        print("\n----- User Profile -----")
        print(f"Name   : {self.__name}")
        print(f"Age    : {self.__age}")
        print(f"Gender : {self.__gender}")
        print(f"Phone  : {self.__phone}")

    # ___________work as a bridge_____________

    #  if someone call the get_user_identity then uit just return the all the data that assign in this method
    def get_user_identity(self):
        return {
            "username": self.get_username(),
            "name": self.get_name() if self.get_name() else self.get_username()
        }
