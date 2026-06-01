from django.contrib import admin
from .models import Author, Book
# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'age', 'book_counter']
    search_fields = ['first_name', 'last_name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','authors_list', 'is_available', 'published_date', 'isbn']
    search_fields = ['title']
    filter_horizontal = ['authors']
    list_filter = ['is_available']

    def authors_list(self, obj):
        return "، ".join(str(author) for author in obj.authors.all())


    authors_list.short_description = 'Authors'