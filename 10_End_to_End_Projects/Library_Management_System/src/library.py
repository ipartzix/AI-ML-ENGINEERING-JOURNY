
from book import Book
from books_data import BOOKS_BY_CATEGORY


class Library:

    def __init__(self, categories=None):
        self.categories = categories

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

    def bookIssue(self, category):
        book_ID = input("\nEnter the book ID to issue this book: ")

        for data in category["books"]:
            if data["id"] == book_ID:
                print(f"\nBook Issued: {data['title']}")
                print("book issue done")
                return True

        print("BOOK NOT FOUND")
        return False

    # ________________book return section________________

    def bookReturn(self):
        print("book return")

    def bookAvailable(self):
        print("Book availability check")

    def dueCalculation(self):
        print("Due calculation")

    def fineCalculation(self):
        print("Fine calculation ")


book = Library()
book.show_categories()

selected_category = book.userBook()

if selected_category:
    book.bookIssue(selected_category)
