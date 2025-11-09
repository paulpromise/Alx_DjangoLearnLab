from django.urls import path
from relationship_app.views import book_list, LibraryDetailView
from . import views

urlpatterns = [
    path("books/", views.book_list, name="book_list"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
]
