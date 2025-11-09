from django.urls import path
from .views import LibraryDetailView
from . import views
from .views import list_books

from django.contrib.auth.views import LoginView, LogoutView
from .views import LibraryDetailView, list_books, register

urlpatterns = [
    path("books/", list_books, name="book_list"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path(
        "login/",
        LoginView.as_view(template_name="relationship_app/login.html"),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="relationship_app/logout.html"),
        name="logout",
    ),
    path("register/", views.register, name="register"),
]
