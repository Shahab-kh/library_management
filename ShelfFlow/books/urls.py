from django.urls import path
from .views import delete_book, edit_book

urlpatterns= [
    path("<int:pk>/delete/", delete_book, name="delete_book"),
    path("<int:pk>/edit/", edit_book, name="edit_book"),
]