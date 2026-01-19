class MemberID:
    def __init__(self):
        self.__username = ""
        self.__password = ""
        # self.__age=""
        # self.__gender =""
        # self.__phone=""

    def menu(self):
        UserID = int(input("""Did you have already Account ?\n
        Enter 1 for YES
        Enter 2 for NO\n"""))
        if UserID == 1:
            print("Welcome back")
        elif UserID == 2:
            print("Create an account")
        else:
            print("Wrong entry!!!!!!")


b = MemberID()
b.menu()
