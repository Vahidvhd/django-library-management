from django.shortcuts import render, redirect
from .models import Author, Book
# Create your views here.
def home(request):
    return render(request, 'library/home.html')


def book_list(request):
    book_list = Book.objects.all()
    context = {'books': book_list}
    return render(request, 'library/book_list.html', context)


def book_detail(request, id):
    book = Book.objects.get(id=id)
    context = {'book': book}
    return render(request, 'library/book_detail.html', context)


def book_add_edit(request, id=None):
    if id:
        book = Book.objects.get(id=id)
    else:
        book = None
    authors = Author.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        author_ids = request.POST.getlist('authors')
        published_date = request.POST.get('published_date')
        is_available = request.POST.get('is_available') == 'on'
        isbn = request.POST.get('isbn')
        summary = request.POST.get('summary')
        
        if book:
            book.title = title
            book.published_date = published_date
            book.isbn = isbn
            book.summary = summary
            book.is_available = is_available
            book.save()

        else:
            book = Book.objects.create(
                title=title,
                published_date=published_date,
                isbn=isbn,
                summary=summary,
                is_available=is_available
            )

        book.authors.set(author_ids)
        return redirect('book_list')












    context = {'book': book, 'authors': authors}
    return render(request, 'library/book_form.html', context)