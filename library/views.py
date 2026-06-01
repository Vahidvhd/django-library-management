from django.shortcuts import render
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