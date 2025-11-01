# Update a book instance
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()

# Expected: The book record with id=1 is updated in the database. 
<Book: Book object (1)>