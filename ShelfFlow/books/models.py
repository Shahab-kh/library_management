from django.db import models
from django.core.exceptions import ValidationError


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    book_code = models.PositiveIntegerField(unique=True)
    cover_image = models.ImageField(upload_to="books/covers/")
    edition = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    total_quantity = models.PositiveIntegerField()
    available_quantity = models.PositiveIntegerField(blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.available_quantity = self.total_quantity
        else:
            old_book = Book.objects.get(pk= self.pk)
            
            borrow = old_book.total_quantity - self.available_quantity
            if self.total_quantity >= borrow:

                if old_book.total_quantity < self.total_quantity:
                    total = self.total_quantity - old_book.total_quantity
                    self.available_quantity += total

                else:
                    total = old_book.total_quantity - self.total_quantity
                    self.available_quantity -= total
            else:
                raise ValidationError("Total quantity cannot be less than borrowed books.")
        super(Book ,self).save(*args, **kwargs)


    def __str__(self):
        return f'{self.title} ( {self.book_code} )'
        