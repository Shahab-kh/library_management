from django.urls import path
from .views import delete_book

urlpatterns= [
    path("<int:pk>/delete/", delete_book, name="delete_book"),
]