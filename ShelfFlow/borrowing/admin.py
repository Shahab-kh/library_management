from django.contrib import admin
from .models import BorrowRecord

class Borrowadmin(admin.ModelAdmin):

    list_display = ['book', 'member', 'borrow_date', 'status']
    fields = ['member', 'book', 'borrow_date']
    readonly_fields = ['borrow_date']
    search_fields = ['member', 'book']
    
admin.site.register(BorrowRecord, Borrowadmin)  
