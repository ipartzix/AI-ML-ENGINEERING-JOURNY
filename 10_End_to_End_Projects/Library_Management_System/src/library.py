from datetime import date, timedelta

from book import Book
from books_data import BOOKS_BY_CATEGORY


class Library:

    # ______________________Constructor________________________


    def __init__(self):
        self.current_user = None  #current_user tracks the logged-in user  || None means no active session.

    # _______________________Display book categories___________________________

    def show_categories(self):
        print("\n_______ Book Categories _______")
        for key, value in BOOKS_BY_CATEGORY.items():
            # key → category identifier (e.g., "1", "2")
            # value → dictionary containing category details

            print(f"key:-{key}. {value['name']}")

    # _____________________user select single domain_______________________

    def show_books_by_category(self):  # update the method name from   userBook() --------> show_books_by_category()

        choice = input("\nEnter category key: ")
        category = BOOKS_BY_CATEGORY.get(choice)  # Fetches category safely. .get() avoids KeyError

        # At first run not case for make code efficient it any error occur then direct code will end  else code run
        if not category:  ## Validate category input and exit early if invalid (guard clause)

            # This prevents unnecessary execution when input is invalid.

            print("Invalid category")
            return None

        print(f"\n{category['name']}")
        for data in category["books"]:
            Book(data["id"], data["title"], data["author"]).display()

        return category  # return the key value the user inputted in previous

    # ______________book issue section_________________

    def bookIssue(self, category):
        if not self.current_user:  # must need to log in to continue the program
            print("Login Required")
            return None

        book_ID = input("\nEnter the book ID to issue this book: ")
        for data in category["books"]:
            if data["id"] == book_ID:
                issue_date = date.today()
                due_date = issue_date + timedelta(days=15)  # implement a dictionary for store issue record

                issue_record = {
                    "username": self.current_user["username"],
                    "name": self.current_user["name"],
                    "book_id": data["id"],
                    "title": data["title"],
                    "issue_date": issue_date,
                    "due_date": due_date,
                    "returned": False
                }
                print(f"\nBook Issued to {self.current_user['name']}")
                print(f"Due Date: {due_date}")
                return issue_record

        print("BOOK NOT FOUND")
        return None


    # ________________book return section________________

    def bookReturn(self):
        if not self.current_user:  # must need to log in to continue the program
            print("Login Required")
            return None

        book_ID = input("\nEnter the book ID to Return : ")
        print(f"\nBook '{data['title']}' returned by {self.current_user['name']}")
        return {
            "username": self.current_user["username"],
            "name": self.current_user["name"],
            "book_id": book_ID,
            "returned": True
        }

    def bookAvailableSearch(self):
        print("Book availability check\n Feature coming soon")

    def dueAndFineCalculation(self):
        print("Due and fine  calculation\n Feature coming soon")
