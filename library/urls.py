from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('book_list/', views.book_list)

]
