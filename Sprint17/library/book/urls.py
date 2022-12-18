from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('add_book/', add_book, name='add_book'),
    path('all_books/', all_books, name='all_books'),
    path('all_books/<int:pk>/', view_book, name='view_book'),
]