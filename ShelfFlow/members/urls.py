from django.urls import path
from .views import delete_member

urlpatterns = [
    path("<int:pk>/delete/", delete_member, name="delete_member"),
]
