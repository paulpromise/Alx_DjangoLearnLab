# Interact with the Model via Django Shell
from bookshelf.models import Book

# View all books in the database and Print their details
books = Book.objects.all()
for book in books:
    print(f"Title: {book.title}, Author: {book.author}, Year: {book.published_year}")

# CRUD Operations Examples
# Add a new book to the database
new_book = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", published_year=1925)
new_book.save()
