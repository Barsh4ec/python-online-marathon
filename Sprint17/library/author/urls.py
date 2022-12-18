from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('all_authors/', show_authors, name='all_authors'),
    path('add_author/', add_author, name='add_author'),
]