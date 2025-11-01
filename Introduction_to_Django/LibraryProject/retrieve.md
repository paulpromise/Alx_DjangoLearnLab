# Retrieve and display all attributes of a book instance
from bookshelf.models import Book
book = Book.objects.get(id=1)
print(book)

# Expected: The book record with id=1 is retrieved from the database.
<Book: Book object (1)>