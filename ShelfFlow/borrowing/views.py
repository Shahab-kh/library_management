from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import BorrowRecord

def return_book(request, pk):
    record = get_object_or_404(BorrowRecord, pk=pk)

    try:
        record.return_book()
        messages.success(request, f"'{record.book.title}' returned successfully.")
    
    except ValidationError as e:
        messages.error(request, e.message)

    return redirect('dashboard')

