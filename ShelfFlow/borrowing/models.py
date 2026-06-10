from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
from books.models import Book
from members.models import Member 


class BorrowRecord(models.Model):

    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)

    borrow_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)

    def clean(self):

        active_borrows = BorrowRecord.objects.filter(
            member = self.member,
            return_date__isnull = True
        ).count()
        
        if self.pk is None and active_borrows >= 5:
            raise ValidationError("Borrow limit reached.")
        
        if self.pk is None and self.book.available_quantity <= 0:
            raise ValidationError("Book not available.")

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        
        if is_new:
            self.due_date = timezone.now() + timedelta(days=14)
        
        self.full_clean()
        super().save(*args, **kwargs)
        
        if is_new: 
            self.book.available_quantity -= 1
            self.book.save()
    
    def return_book(self):
        if self.return_date is not None:
            raise ValidationError('Book already returned.')
        
        self.return_date = timezone.now()
        self.book.available_quantity += 1
        self.book.save()
        self.save(update_fields=["return_date"])
    
    @property
    def status(self):
        if self.return_date:
            return 'Returned'
        
        elif timezone.now() > self.due_date:
            return 'Overdue'
        
        return 'Borrowed'