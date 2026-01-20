from books_data import BOOKS_BY_CATEGORY


class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    # ______________________display a single book object_______________________

    def display(self):
        print(f"[{self.book_id}] {self.title} - {self.author}")

    # _______________________Display book categories___________________________

    def show_categories(self):
        print("\n_______ Book Categories _______")
        for key, value in BOOKS_BY_CATEGORY.items():
            print(f"{key}. {value['name']}")


book = Book("CS101", "Introduction to Algorithms", "Cormen")
book.display()
