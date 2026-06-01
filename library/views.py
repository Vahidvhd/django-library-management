from django.shortcuts import render
from .models import Author, Book
# Create your views here.
def home(request):
    return render(request, 'library/home.html')


def book_list(request):
    book_list = Book.objects.all()
    context = {'books': book_list}
    return render(request, 'library/book_list.html', context)