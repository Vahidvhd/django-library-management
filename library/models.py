from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def book_counter(self):
        return self.books.count()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, related_name='books')
    published_date = models.DateField()
    is_available = models.BooleanField(default=True)
    isbn = models.CharField(max_length=13, unique=True)
    summary = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
    def clean(self):
        if self.isbn and len(self.isbn) != 13 or not self.isbn.isdigit():
            raise ValidationError({'isbn':'Invalid ISBN'})
        if self.published_date and self.published_date > timezone.now().date():
            raise ValidationError({'published_date': 'Published date cannot be in the future.'})

    