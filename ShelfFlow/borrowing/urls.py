from django.urls import path
from .views import return_book

urlpatterns = [
    path('<int:pk>/return/', return_book, name="return_book"),
]


