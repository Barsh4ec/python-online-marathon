from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from django.contrib.auth import login, logout

def home_page(request):
    return render(request, 'home_page.html')


