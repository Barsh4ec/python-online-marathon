from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('all_users/', all_users, name='all_users'),
]