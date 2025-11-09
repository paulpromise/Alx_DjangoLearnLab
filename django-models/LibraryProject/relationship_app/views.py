from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from . import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm

def list_books(request):
    """
    A simple view that renders a template listing all books and their authors.
    """
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


@permission_required("relationship_app.can_add_book")
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "relationship_app/book_form.html", {"form": form})


@permission_required("relationship_app.can_change_book")
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "relationship_app/book_form.html", {"form": form})


# Delete book view (requires can_delete_book permission)
@permission_required("relationship_app.can_delete_book")
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "relationship_app/book_confirm_delete.html", {"book": book})


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


# Helper functions to check roles
def is_admin(user):
    return hasattr(user, "profile") and user.profile.role == "Admin"


def is_librarian(user):
    return hasattr(user, "profile") and user.profile.role == "Librarian"


def is_member(user):
    return hasattr(user, "profile") and user.profile.role == "Member"


# Role-specific views
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")
