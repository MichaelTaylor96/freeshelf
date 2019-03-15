from django.shortcuts import render
from .models import Book
from .forms import FilterSort, Search
from django.core.paginator import Paginator

# Create your views here.

def index(request):   
    if request.GET:
        filtersortform = FilterSort(request.GET)
        searchform = Search(request.GET)
        books = searchform.search(Book.objects.all())
        books = filtersortform.filtersort(books)
    else:
        filtersortform = FilterSort()
        searchform = Search()
        books = Book.objects.all()

    sorter = request.GET.get('sorter', '-added_at')
    paginator = Paginator(books, 16)
    page = request.GET.get('page', 1)
    books = paginator.get_page(page)

    return render(request, 'core/index.html', context={'books': books, 'filtersort': filtersortform, 'search': searchform, 'sorter': sorter})

def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'core/book_detail.html', context={'book':book})
