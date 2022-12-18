from django.shortcuts import render, redirect
from django.contrib import messages
from book.models import Book
from author.models import Author
from django.shortcuts import get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError


def add_book(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        count = request.POST['count']
        photo = request.FILES['photo']

        book = Book.objects.create(name=name, description=description, photo=photo, count=count)

        try:
            if request.POST['with_book'] == 'on':
                return redirect('all_books')
            else:
                author_id = request.POST['authors']
                author = Book.get_by_id(author_id)
                book.add_authors(author)
                return redirect('all_books')
        except MultiValueDictKeyError:
            author_id = request.POST['authors']
            author = Author.get_by_id(author_id)
            book.add_authors(author)
            return redirect('all_books')
    context = {'authors': Author.get_all()}
    return render(request, 'add_book.html', context)


def all_books(request):
    books = list(Book.objects.all())
    authors = Author.books
    if request.method == 'POST':
        searchpattern = request.POST['input']
        if request.POST['selector'] == '1':
            books = list(Book.objects.filter(authors__icontains=searchpattern))
        elif request.POST['selector'] == '2':
            books = list(Book.objects.filter(name__icontains=searchpattern))
        elif request.POST['selector'] == '3':
            books = list(Book.objects.filter(description__icontains=searchpattern))
    context = {
            'books': books,
            'authors': authors
        }
    return render(request, 'all_books.html', context)

def view_book(request, pk):
    books_item = Book.objects.get(pk=pk)
    authors = Author.books
    return render(request, 'view_book.html', {'books_item': books_item, 'authors': authors})