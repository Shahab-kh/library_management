from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Book
from members.models import Member
from borrowing.forms import BorrowForm
from borrowing.models import BorrowRecord

def book_list(request):
    query = request.GET.get("q")
    books = Book.objects.all()
    members = Member.objects.all() 
    borrow_form = BorrowForm()
    

    if request.method == "POST":

        book_id = request.POST.get("book")
        book = get_object_or_404(Book, id=book_id)

        borrow = BorrowRecord(book=book)

        borrow_form = BorrowForm(
            request.POST,
            instance=borrow
        )

        if borrow_form.is_valid():

            borrow_form.save()

            messages.success(
                request,
                "Book borrowed successfully."
            )

            return redirect("book_list")

        else:

            for error in borrow_form.non_field_errors():
                messages.error(request, error)

    if query :
        books = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) 
        )

    return render(
    request,
    "books/book_list.html",
    {
        "books": books,
        "members": members,
        "borrow_form": borrow_form,
    }
)


