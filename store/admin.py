from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
   list_display = ('id', 'title', 'author', 'description', 'publish_date')

admin.site.register(Book, BookAdmin)