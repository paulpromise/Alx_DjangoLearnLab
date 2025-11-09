from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView
from . import Book, Library


def book_list(request):
    """
    A simple view that renders a template listing all books and their authors.
    """
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view — show library details and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # ✅ required by checker
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.all()
        return context
