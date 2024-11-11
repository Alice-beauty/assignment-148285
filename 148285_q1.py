# Define the Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

# Define the LibraryMember class
class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            if book.mark_as_borrowed():
                self.borrowed_books.append(book)
                print(f"{self.name} successfully borrowed '{book.title}'.")
            else:
                print(f"Failed to borrow '{book.title}' - it's already borrowed.")
        else:
            print(f"'{book.title}' is currently borrowed by someone else.")

    def return_book(self, book):
        if book in self.borrowed_books:
            if book.mark_as_returned():
                self.borrowed_books.remove(book)
                print(f"{self.name} successfully returned '{book.title}'.")
            else:
                print(f"Failed to return '{book.title}'.")
        else:
            print(f"{self.name} does not have '{book.title}' to return.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name}'s Borrowed Books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.name} has no borrowed books.")

def main():
    # Create sample books
    book1 = Book("The Alchemist", "Paulo Coelho")
    book2 = Book("The 7 Habits", "Stephen R. Covey.")

    # Create library member
    member = LibraryMember("Alice", "M123")

    # Borrow books
    member.borrow_book(book1)
    member.borrow_book(book2)

    # List borrowed books
    member.list_borrowed_books()

    # Return a book
    member.return_book(book1)

    # List borrowed books again
    member.list_borrowed_books()

# Run the sample code
main()
