from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from books.forms import BookForm
from books.models import Book


def books(request):
    book_list = Book.objects.all()
    context = {
        'book_list': book_list,
    }
    return render(request, 'books.html', context)


def add_book(request):
    context = {
        'bookform': BookForm(),
    }
    return render(request, 'addbook.html', context)


def add_book_action(request):
    bookform = BookForm(request.POST, request.FILES)
    if bookform.is_valid():
        bookform.save()
        return redirect('books:books')
    else:
        context = {
            'bookform': bookform,
        }
        return render(request, 'addbook.html', context)

def find_book(request):
    return HttpResponse("BOOK FOUND")


def delete_book(request):
    return HttpResponse("BOOK DELETED")

def single_book(request, pk):
    book = Book.objects.get(id=pk)
    return render(request, "single_book.html",{'book':book})
    
