from django.db import models


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
            
        super(Book ,self).save(*args, **kwargs)


    def __str__(self):
        return f'{self.title} ( {self.book_code} )'
        