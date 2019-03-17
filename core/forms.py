from django import forms
from .models import Book, Author, Category, Comment

class FilterSort(forms.Form):
    sorter = forms.ChoiceField(
        label="Sort by",
        choices=[('-added_at', '-----'),
                ('author__name', 'Author'),
                ('added_at', 'Date'),
                ('title', 'Title'),],
        required=False)

    category = forms.ChoiceField(
        label="Category",
        choices=[('none', '-----')]+[(str(category.name), str(category.name)) for category in Category.objects.all()],
        required=False)

    def filtersort(self, books):
        if not self.is_valid():
            return None

        data = self.cleaned_data

        if data['category'] and data['category'] != 'none':
            books = books.filter(categories__name__iexact=data['category'])

        if not data['sorter']:
            data['sorter'] = '-added_at'
        books = books.order_by(data['sorter'])

        return books

class Search(forms.Form):

    search_by = forms.ChoiceField(
        label="Search by",
        choices=[('title', 'Title'),
                ('author__name', 'Author'),],
        required=False)

    search_for = forms.CharField(
        label="Search for",
        required=False,
    )

    def search(self, books):
        if not self.is_valid():
            return None

        data = self.cleaned_data

        if data['search_by'] and data['search_for']:
            books = books.filter(**{f"{data['search_by']}__icontains":data['search_for']})

        return books

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user']
        widgets = {'book': forms.HiddenInput()}
        