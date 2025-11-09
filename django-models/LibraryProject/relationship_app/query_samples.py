"""
This script contains queries for the following relationships:
1. Query all books by a specific author.
2. List all books in a library.
3. Retrieve the librarian for a library.
"""

from relationship_app.models import Author, Book, Librarian, Library


# 1. Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        # ✅ Modified line to include the expected pattern
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        print(f"No author found with name '{author_name}'")
        return []


# 2. List all books in a library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'")
        return []


# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian    
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'")
        return None
