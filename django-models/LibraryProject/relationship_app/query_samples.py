"""
This script should contain the query for each of the following of relationship:
Query all books by a specific author.
List all books in a library.
Retrieve the librarian for a library.
"""

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author.
author = Author.objects.get(name="Author Name")
books_by_author = author.books.all()

# List all books in a library.
library = Library.objects.get(name="Library Name")
books_in_library = library.books.all()

# Retrieve the librarian for a library.
librarian = library.librarian