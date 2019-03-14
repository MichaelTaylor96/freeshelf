from django import forms
from .models import Book

class BookSort(forms.Form):
    sorter = forms.ChoiceField(
        label="Sort by",
        choices=[('author__name', 'Author'),
                ('added_at', 'Date'),
                ('title', 'Title'),
                ('-added_at', 'None')],
        required=False)

    def sort(self):
        if not self.is_valid():
            return None

        data = self.cleaned_data
        if not data['sorter']:
            data['sorter'] = '-added_at'
        books = Book.objects.order_by(data['sorter'])
        return books

        
        
