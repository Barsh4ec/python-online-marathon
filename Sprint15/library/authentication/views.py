from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from authentication.models import CustomUser
from django.utils.datastructures import MultiValueDictKeyError


def user_register(request):
    if request.method == 'POST':
        print(request.POST['second-password'])
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        is_active = True
        if request.POST['password'] == request.POST['second-password']:
            try:
                if request.POST['role'] == 'on':
                    role = 1
                else:
                    role = 0
            except MultiValueDictKeyError:
                role = 0
            user = CustomUser.objects.create_user(email=email, password=password, first_name=first_name,
                                                  middle_name=middle_name, last_name=last_name, role=role, is_active=is_active)
            if user:
                messages.success(request, 'Ви успіщно зареєструвались!')
                return redirect('login')
            else:
                messages.error(request, 'Щось пішло не так!')
        else:
            messages.error(request, 'Ви ввели різні паролі!')
    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Ви успіщно зареєструвались!')
            return redirect('home')
        else:
            messages.error(request, 'Щось пішло не так!')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')


def all_users(request):
    users = CustomUser.objects.all()
    if request.method == 'POST':
        user_id = request.POST['input']
        users = CustomUser.objects.get(pk=user_id)
        return render(request, 'show_user.html', context={'user': users})
    return render(request, 'all_users.html', context={'users': users})