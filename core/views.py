from django.shortcuts import render
from .models import Book
from .forms import BookSort

# Create your views here.

def index(request):   
    if request.GET:
        form = BookSort(request.GET)
        books = form.sort()
    else:
        form = BookSort()
        books = books = Book.objects.all()

    return render(request, 'core/index.html', context={'books': books, 'sort': form})
