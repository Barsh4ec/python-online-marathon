from django.shortcuts import render, redirect
from django.contrib import messages
from author.models import Author
from book.models import Book
from django.utils.datastructures import MultiValueDictKeyError

def show_authors(request):
    if request.method == 'POST':
        Author.delete_by_id(request.POST['author_id'])
    authors = Author.objects.prefetch_related('books').all()
    for author in authors:
        book = author.books.all()
        if book:
            author.book = book[0].name
        else:
            author.book = None
    context = {
            'authors': authors,
        }
    return render(request, 'show_authors.html', context)


def add_author(request):
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        patronymic = request.POST['patronymic']

        author = Author.objects.create(name=name, surname=surname, patronymic=patronymic)
        try:
            if request.POST['with_book'] == 'on':
                return redirect('all_authors')
            else:
                book_id = request.POST['book']
                book = Book.get_by_id(book_id)
                author.books.add(book)
                return redirect('all_authors')
        except MultiValueDictKeyError:
            book_id = request.POST['book']
            book = Book.get_by_id(book_id)
            author.books.add(book)
            return redirect('all_authors')
    context = {'books': Book.get_all()}
    return render(request, 'add_author.html', context)