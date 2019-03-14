from django.shortcuts import render
from .models import Book
from .forms import BookSort
from django.core.paginator import Paginator

# Create your views here.

def index(request):   
    if request.GET:
        form = BookSort(request.GET)
        books = form.sort()
    else:
        form = BookSort()
        books = Book.objects.all()

    sorter = request.GET.get('sorter', '-added_at')
    paginator = Paginator(books, 16)
    page = request.GET.get('page', 1)
    books = paginator.get_page(page)

    return render(request, 'core/index.html', context={'books': books, 'sort': form, 'sorter': sorter})
