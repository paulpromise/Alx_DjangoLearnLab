# Import the Book model
from bookshelf.models import Book


# Create a new book instance
book = Book(title="1994", author="F. Scott Fitzgerald", published_year=1925)
book.save()

# Expected: A new book record is created in the database with the provided details.
<bound method Model.save of <Book: Book object (None)>>




