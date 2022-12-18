from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from authentication.models import CustomUser
from rest_framework import viewsets
from .serializers import CustomUserSerializer
from .forms import UserRegisterForm, UserLoginForm, SearchUserForm
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response



def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = CustomUser.objects.create_user(**form.cleaned_data, is_active=True)
            if user:
                messages.success(request, 'Ви успіщно зареєструвались!')
                return redirect('login')
        else:
            messages.error(request, 'Щось пішло не так!')
        form = UserRegisterForm(request.POST)
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, email=request.POST['email'], password=request.POST['password'])
            if user:
                login(request, user)
                return redirect('home')
        form = UserLoginForm(request.POST)
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {"form": form})

def user_logout(request):
    logout(request)
    return redirect('home')


def all_users(request):
    users = CustomUser.objects.all()
    if request.method == 'POST':
        form = SearchUserForm(request.POST)
        if form.is_valid():
            user_id = request.POST['input']
            users = CustomUser.objects.get(pk=int(user_id))
            return render(request, 'show_user.html', context={'user': users})
    else:
        form = SearchUserForm()
    return render(request, 'all_users.html', context={'users': users, "form": form})


class CustomUserView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

