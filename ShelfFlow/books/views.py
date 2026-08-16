from django.shortcuts import render
from django.db.models import Q
from .models import Book

def book_list(request):
    query = request.GET.get("q")
    books = Book.objects.all()

    if query :
        books = Book.objects.filter(
            Q(title__icontains=query) or
            Q(author__icontains=query) 
        )

    return render(request, "books/book_list.html", { "books" : books })

# books/book_list.html
