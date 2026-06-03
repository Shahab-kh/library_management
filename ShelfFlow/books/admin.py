from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'book_code']
    fields = ['title', 'author', 'book_code', 'edition','cover_image', 'description', 'total_quantity']

admin.site.register(Book, BookAdmin)