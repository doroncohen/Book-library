from django.contrib import admin
from .models import Book, IssuedItem

# Register the Book model with the admin site
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'author_name', 'quantity', 'subject', 'book_add_date', 'book_add_time')

# Register the IssuedItem model with the admin site
@admin.register(IssuedItem)
class IssuedItemAdmin(admin.ModelAdmin):
    list_display = ('book_id', 'user_id', 'issue_date', 'return_date')