# Retrieve and display all attributes of a book instance
from bookshelf.models import Book

book = Book.objects.get(id=1)
print(book.title, book.author, book.published_year)


# Expected: The book record with id=1 is retrieved from the database.
1984 George Orwell 1949


