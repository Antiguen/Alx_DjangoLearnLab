from django.contrib import admin
from .models import Book # <-- THIS LINE IS CRUCIAL

# Define the custom configuration for the Book model in the admin
class BookAdmin(admin.ModelAdmin):
    # 1. Customize the list display: show title, author, and publication_year
    list_display = ('title', 'author', 'publication_year')

    # 2. Configure list filters: allow filtering by author and publication_year
    list_filter = ('author', 'publication_year')

    # 3. Configure search capabilities: allow searching by title and author
    search_fields = ('title', 'author')

    # Optional: Order the books by publication year descending
    ordering = ('-publication_year',)

# Register the Book model with the custom BookAdmin class
admin.site.register(Book, BookAdmin)