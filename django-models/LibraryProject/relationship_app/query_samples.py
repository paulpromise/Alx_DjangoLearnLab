"""
This script contains queries for the following relationships:
1. Query all books by a specific author.
2. List all books in a library.
3. Retrieve the librarian for a library.
"""

from relationship_app.models import Author, Library


# 1. Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
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
        return getattr(library, "librarian", None)
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'")
        return None

