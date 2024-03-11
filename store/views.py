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


def new_book(request):
    print(request.method)
    context = {
        'title': 'New Book',
        'book': {
            'title': '',
            'author': '',
            'description': '',
            'publish_date': '',
            'price': '',
            'stock': '',
        },
        'form_action': 'new_book',
    }
    if request.method == 'POST':
        try:
            # Extract data from POST request
            title = request.POST.get('title')
            author = request.POST.get('author')
            description = request.POST.get('description')
            publish_date = request.POST.get('pubdate')
            price = request.POST.get('price')
            stock = request.POST.get('stock')

            # Create a new Book object using extracted data
            Book.objects.create(
                title=title,
                author=author,
                description=description,
                publish_date=publish_date,
                price=price,
                stock=stock
            )

            # Optionally, you can return a response indicating success
            context['message'] = 'The book has been created.'

        except Exception as e:
            # Handle exceptions, e.g., invalid data format or missing required fields
            context['message'] = 'Error creating book, please try again later.'

    return render(request, 'store/book_form.html', context)


def book_details(request, id):
    book = Book.objects.get(id=id)
    context = {
        'title': 'Book Details',
        'book': book,
    }
    return render(request, 'store/book_details.html', context)


def edit_book(request, id):
    book = Book.objects.get(id=id)
    context = {
        'title': 'Edit Book',
        'book': book,
        'id': id,
        'form_action': 'edit_book',
    }

    if request.method == 'POST':
        try:
            # Extract data from POST request
            book = Book.objects.get(id=id)

            book.title = request.POST.get('title')
            book.author = request.POST.get('author')
            book.description = request.POST.get('description')
            book.publish_date = request.POST.get('pubdate')
            book.price = request.POST.get('price')
            book.stock = request.POST.get('stock')
            book.save()
            context['message'] = 'The book has been updated.'
        except:
            context['message'] = 'Update failed. Try again later.'

    return render(request, 'store/book_form.html', context)
