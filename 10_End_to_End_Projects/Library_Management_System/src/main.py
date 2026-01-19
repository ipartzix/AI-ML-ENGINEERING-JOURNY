from member import UserData

user1 = UserData()

while True:
    success = user1.menu()

    if success:
        choice = input("Press 1 to continue, 0 to exit: ")
        if choice == "0":
            print("Exiting program.")
            break
    else:
        print("Try again.")
