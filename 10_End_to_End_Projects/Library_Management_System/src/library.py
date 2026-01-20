from books_data import BOOKS_BY_CATEGORY


class Library:

    def __init__(self, categories=None):
        self.categories = categories

    # _______________________Display book categories___________________________

    def show_categories(self):
        print("\n_______ Book Categories _______")
        for key, value in BOOKS_BY_CATEGORY.items():
            print(f"{key}. {value['name']}")

    def bookIssue(self):
        print("book issue done")

    def bookReturn(self):
        print("book return")

    def bookAvailable(self):
        print("Book availability check")

    def dueCalculation(self):
        print("Due calculation")

    def fineCalculation(self):
        print("Fine calculation ")


book = Library()
book.bookIssue()
