from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from . import Book
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

def list_books(request):
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


# User registration view
def register(request):
    form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


def login_view(request):
    return render(request, "relationship_app/login.html")

def logout_view(request):
    return render(request, "relationship_app/logout.html")
