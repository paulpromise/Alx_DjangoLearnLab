# Import the Book model
from bookshelf.models import Book

# Create a new book instance directly in the database
Book.objects.create(title="1984", author="George Orwell", published_year=1949)
book.save()

# Expected: A new book record is created in the database with the provided details.
<Book: Book object (None)>




    