from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST
from .models import BorrowRecord

@require_POST
def return_book(request, pk):
    record = get_object_or_404(BorrowRecord, pk=pk)

    try:
        record.return_book()
        messages.success(request, f"'{record.book.title}' returned successfully.")
    
    except ValidationError as e:
        messages.error(request, e.message)

    return redirect('dashboard')

