from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'book_code']
    readonly_fields = ['available_quantity']
    search_fields = ['title', 'author', 'book_code']

admin.site.register(Book, BookAdmin)