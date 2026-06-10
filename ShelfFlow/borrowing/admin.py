from django.contrib import admin
from .models import BorrowRecord

class Borrowadmin(admin.ModelAdmin):

    list_display = ['book', 'member', 'borrow_date', 'status']
    fields = ['member', 'book']
    
admin.site.register(BorrowRecord, Borrowadmin)
