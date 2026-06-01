from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('book_list/', views.book_list, name = 'book_list'),
    path('book_detail/<int:id>/', views.book_detail, name= 'book_detail'),
    path('book_add_edit/', views.book_add_edit, name= 'book_add_edit'),
    path('book_add_edit/<int:id>/', views.book_add_edit, name= 'book_add_edit')
]
