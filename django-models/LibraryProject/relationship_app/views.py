from django.http import HttpResponse
from django.views.generic import DetailView
from relationship_app.models import Book, Library


def book_list(request):
    """
    A simple view that returns a plain-text list of all books and their authors.
    """
    books = Book.objects.all()

    if not books.exists():
        return HttpResponse("No books found.", content_type="text/plain")

    output = "\n".join([f"{book.title} — {book.author.name}" for book in books])
    return HttpResponse(output, content_type="text/plain")


# Class-based view — show library details and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/list_books.html"  # ✅ change this
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.all()
        return context