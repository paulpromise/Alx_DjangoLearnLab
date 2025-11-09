# Delete a book instance
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.delete()

# Expected: The book record with id=1 is deleted from the database.
(1, {'bookshelf.Book': 1})  