from django.shortcuts import render
from .models import Book

# Create your views here.


def index(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'store/template.html', context)


def store(request):
    books = Book.objects.all()
    context = {
        'books': books,
        'count': books.count(),
        'title': 'Store',
    }
    return render(request, 'store/store.html', context)
