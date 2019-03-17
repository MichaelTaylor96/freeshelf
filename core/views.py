from django.shortcuts import redirect, render
from .models import Book
from .forms import FilterSort, Search, CommentForm
from django.core.paginator import Paginator
from django.contrib import messages

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

    if request.method == "POST" and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            messages.success(
                request,
                f"Thank you for your input!"
            )
            return redirect(to='Book_detail', slug=book.slug)

    form = CommentForm(initial={"book": book})
    
    return render(request, 'core/book_detail.html', context={'book':book, 'form':form})
