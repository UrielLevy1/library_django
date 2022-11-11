from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
   path('', views.books, name="books"),
   path('add/', views.add_book, name="add"),
   path('add_book_action/', views.add_book_action, name="add_book_action"),
   path('search/', views.find_book, name="search"),
   path('delete/', views.delete_book, name="delete"),
   path('<pk>/', views.single_book, name="single_book"),

   
]
