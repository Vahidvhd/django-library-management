from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name= 'home'),
    path('book_list/', views.book_list, name = 'book_list'),
    path('book_detail/<int:id>/', views.book_detail, name= 'book_detail'),
    path('book_add_edit/', views.book_add_edit, name= 'book_add_edit'),
    path('book_add_edit/<int:id>/', views.book_add_edit, name= 'book_add_edit'),
    path('author_add/', views.author_add, name = 'author_add'),
    path('author_list/', views.author_list, name = 'author_list'),
    path('book_delete/<int:id>/', views.book_delete, name="book_delete")
]
