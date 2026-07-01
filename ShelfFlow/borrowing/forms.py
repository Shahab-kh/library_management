from django import forms
from .models import BorrowRecord

class BorrowForm(forms.ModelForm):
    class Meta:
        model = BorrowRecord
        fields = [
            'member',
            'book',
            ]
