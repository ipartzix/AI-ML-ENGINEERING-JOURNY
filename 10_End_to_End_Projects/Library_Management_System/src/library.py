from datetime import date, timedelta

from book import Book
from books_data import BOOKS_BY_CATEGORY


class Library:

    def __init__(self, categories=None):
        self.categories = categories
        self.current_user = None

    # _______________________Display book categories___________________________

    def show_categories(self):
        print("\n_______ Book Categories _______")
        for key, value in BOOKS_BY_CATEGORY.items():
            print(f"key:-{key}. {value['name']}")

    # _____________________user select single domain_______________________



    def userBook(self):
        choice = input("\nEnter category key: ")
        category = BOOKS_BY_CATEGORY.get(choice)

        if not category:
            print("Invalid category")
            return None

        print(f"\n{category['name']}")
        for data in category["books"]:
            Book(data["id"], data["title"], data["author"]).display()

        return category

    # ______________book issue section_________________

    def bookIssue(self, get_username, get_password, category):
        if get_username():
            get_password():
            self.__username
            print("Login Required ")
            return None
        else:
            book_ID = input("\nEnter the book ID to issue this book: ")

            for data in category["books"]:
                if data["id"] == book_ID:
                    issue_date = date.today()
                    due_date = issue_date + timedelta(days=15)  # implement a dictionary for store issue record
                    issue_record = {
                        "__username": self.current_user["name"],
                        "book_id": data["id"],
                        "title": data["title"],
                        "issue_date": issue_date,
                        "due_date": due_date,
                        "returned": False
                    }
                    print(f"\nBook Issued to {self.current_user['name']}")
                    print(f"Due Date: {due_date}")

                    return issue_record
                return True
            print("BOOK NOT FOUND")
            return False
        if not self.current_user:
            print("Login Required ")
            return None



    # ________________book return section________________

    def bookReturn(self):
        print("book return")

    def bookAvailable(self):
        print("Book availability check")

    def ueAndFineCalculation(self):
        print("Due and fine  calculation")



