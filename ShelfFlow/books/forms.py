from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'book_code',
            'edition',
            'cover_image',
            'description',
            'total_quantity',
                ]
