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

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.mark_as_borrowed():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}.")
        else:
            print(f"{book.title} is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books and book.mark_as_returned():
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} does not have {book.title}.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.name} has not borrowed any books.")

def main():
    # Create some books
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

    # Create a library member
    member = LibraryMember("Alice", 1)

    # Borrow and return books
    member.borrow_book(book1)
    member.borrow_book(book2)
    member.list_borrowed_books()
    member.return_book(book1)
    member.list_borrowed_books()

if __name__ == "__main__":
    main()
