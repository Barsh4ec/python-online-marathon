from django.shortcuts import render, redirect
from book.models import Book
from author.models import Author
from django.utils.datastructures import MultiValueDictKeyError
from .forms import CreateBookForm, SearchBookForm
from rest_framework import viewsets
from .serializers import BookSerializer


def add_book(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        name = request.POST['name']
        description = request.POST['description']
        count = request.POST['count']
        photo = request.FILES['photo']
        if form.is_valid():
            book = Book.objects.create(name=name, description=description, photo=photo, count=count)

            try:
                if request.POST['checkbox'] == 'on':
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
    else:
        form = CreateBookForm(request.POST)
    return render(request, 'add_book.html', {'authors': Author.get_all(), "form": form})


def all_books(request):
    books = list(Book.objects.all())
    authors = Author.books
    if request.method == 'POST':
        form = SearchBookForm(request.POST)
        if form.is_valid():
            searchpattern = request.POST['input']
            if request.POST['selector'] == '1':
                books = list(Book.objects.filter(authors__name__icontains=searchpattern))
            elif request.POST['selector'] == '2':
                books = list(Book.objects.filter(name__icontains=searchpattern))
            elif request.POST['selector'] == '3':
                books = list(Book.objects.filter(description__icontains=searchpattern))
    else:
        form = SearchBookForm()
    context = {
        'books': books,
        'authors': authors,
        'form': form
    }
    return render(request, 'all_books.html', context)



def view_book(request, pk):
    books_item = Book.objects.get(pk=pk)
    authors = Author.books
    return render(request, 'view_book.html', {'books_item': books_item, 'authors': authors})


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer