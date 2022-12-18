
from django.urls import path, include
from .views import *

urlpatterns = [
    path('all_orders/', all_orders, name='all_orders'),
    path('my_orders/', my_orders, name='my_orders'),
    path('add_order/', add_order, name='add_order'),
]