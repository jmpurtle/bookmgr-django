from django.contrib import admin
from .models import Book, Genre, Subject

class BookAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Book._meta.fields]

admin.site.register(Book, BookAdmin)