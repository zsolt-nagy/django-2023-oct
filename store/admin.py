from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'description',
                    'publish_date', 'price', 'stock')


admin.site.register(Book, BookAdmin)
