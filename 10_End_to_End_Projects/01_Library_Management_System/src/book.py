class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    # ______________________display a single book object_______________________

    def display(self):
        print(f"[{self.book_id}] {self.title} - {self.author}")

# book = Book("CS101", "Introduction to Algorithms", "Cormen")
# book.display()
