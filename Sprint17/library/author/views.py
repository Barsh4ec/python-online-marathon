from django.shortcuts import render, redirect
from django.contrib import messages
from author.models import Author
from book.models import Book
from django.utils.datastructures import MultiValueDictKeyError
from .forms import CreateAuthorForm
from rest_framework import viewsets
from .serializers import AuthorSerializer


def show_authors(request):
    if request.method == 'POST':
        Author.delete_by_id(request.POST['author_id'])
    authors = Author.objects.prefetch_related('books').all()
    for author in authors:
        book = author.books.all()
        if book:
            author.book = book
        else:
            author.book = None
    context = {
            'authors': authors,
        }
    return render(request, 'show_authors.html', context)


def add_author(request):
    if request.method == 'POST':
        form = CreateAuthorForm(request.POST)
        name = request.POST['name']
        surname = request.POST['surname']
        patronymic = request.POST['patronymic']
        if form.is_valid():
            author = Author.objects.create(name=name, surname=surname, patronymic=patronymic)
        try:
            if request.POST['checkbox'] == 'on':
                return redirect('all_authors')
            else:
                book_id = request.POST['books']
                book = Book.get_by_id(book_id)
                author.books.add(book)
                return redirect('all_authors')
        except MultiValueDictKeyError:
            book_id = request.POST['books']
            book = Book.get_by_id(book_id)
            author.books.add(book)
            return redirect('all_authors')
    else:
        form = CreateAuthorForm(request.POST)
    return render(request, 'add_author.html', {'books': Book.get_all(), "form": form})


class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer