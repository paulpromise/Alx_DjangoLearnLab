# Import the Book model
from bookshelf.models import Book


# Create a new book instance
book = Book(title="1994", author="F. Scott Fitzgerald", published_year=1925)
book.save()

# Expected: A new book record is created in the database with the provided details.
<bound method Model.save of <Book: Book object (None)>>




# Retrieve and display all attributes of a book instance
from bookshelf.models import Book
book = Book.objects.get(id=1)
print(book)

# Expected: The book record with id=1 is retrieved from the database.
<Book: Book object (1)>


# Update a book instance
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()

# Expected: The book record with id=1 is updated in the database. 
<Book: Book object (1)>


# Delete a book instance
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.delete()

# Expected: The book record with id=1 is deleted from the database.
(1, {'bookshelf.Book': 1})  