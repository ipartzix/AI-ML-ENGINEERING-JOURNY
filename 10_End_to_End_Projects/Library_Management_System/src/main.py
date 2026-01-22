from library import Library
from member import UserData


def main():
    # Initialize the core components
    user = UserData()
    library = Library()

    print("=== Welcome to the Library Management System ===")

    # Step 1: Authentication (Login or Create Account)
    # user.menu() returns True if the user successfully logs in or signs up
    if user.menu():
        # Step 2: Extract identity and pass it to the library
        # This allows the library to track who is issuing books
        library.current_user = user.get_user_identity()

        while True:
            print("\n" + "=" * 30)
            print(f"Logged in as: {library.current_user['name']}")
            print("1. Browse Book Categories")
            print("2. Return a book ")
            print("3. Exit")

            choice = input("Select an option: ")

            # _____________________book selection section____________________________

            if choice == "1":
                # Display all available categories from books_data.py
                library.show_categories()

                # Let user pick a category and view its books
                category = library.show_books_by_category()  # update the method name from   userBook() --------> show_books_by_category()

                if category:
                    # Ask if they want to issue a book from the displayed list
                    issue_prompt = input("\nWould you like to issue a book? (y/n): ")
                    if issue_prompt.lower() == 'y':
                        # library.bookIssue returns a record dictionary if successful
                        record = library.bookIssue(category)
                        if record:
                            print(f"\nSUCCESS: '{record['title']}' must be returned by {record['due_date']}.")


            elif choice == "2":
                library.bookReturn()  # no category needed


            elif choice == "3":
                print(f"Goodbye, {library.current_user['name']}!")
                break
            else:
                print("Invalid input. Please try again.")
    else:
        print("Access denied. Please restart the program to try again.")


if __name__ == "__main__":
    main()
