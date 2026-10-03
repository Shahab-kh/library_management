from django.urls import path
from .views import delete_member, edit_member

urlpatterns = [
    path("<int:pk>/edit/", edit_member, name="edit_member"),
    path("<int:pk>/delete/", delete_member, name="delete_member"),
]
