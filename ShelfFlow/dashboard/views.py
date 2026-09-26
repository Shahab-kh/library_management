from django.shortcuts import render
from members.models import Member
from books.models import Book

def dashboard(request):
    members = Member.objects.all()
    books = Book.objects.all()
    return render(request, "dashboard/dashboard.html", {'members': members, 'books': books})
