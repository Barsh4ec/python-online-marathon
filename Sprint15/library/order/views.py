from django.shortcuts import render, redirect
from django.contrib import messages
from order.models import Order
from book.models import Book
from authentication.models import CustomUser
from django.utils.datastructures import MultiValueDictKeyError
import time


def add_order(request):
    if request.method == 'POST':
        book_id = request.POST['book_id']
        user_id = request.POST['user_id']
        planed_end_at = request.POST['planed_end_at']

        book = Book.get_by_id(book_id)
        user = CustomUser.get_by_id(user_id)

        Order.create(user, book, planed_end_at)
        return redirect('all_orders')

    books = Book.get_all()
    users = CustomUser.get_all()
    context = {
        'books': books,
        'users': users
    }
    return render(request, 'add_order.html', context)


def all_orders(request):
    try:
        if request.method == 'POST':
            user_id = request.POST['input']
            orders = Order.objects.filter(user=user_id)
            return render(request, 'all_orders.html', context={'orders': list(orders)})
    except MultiValueDictKeyError:
        if request.method == 'POST':
            order = Order.get_by_id(request.POST['order_id'])
            order.update(end_at=time.strftime("%Y-%m-%d %H:%M", time.gmtime(time.time())))
    orders = list(Order.objects.all())
    context = {
            'orders': orders,
        }
    return render(request, 'all_orders.html', context)


def my_orders(request):
    orders = Order.objects.select_related().filter(user_id=request.user.id).values('id',
                                                                                   'user__first_name',
                                                                                   'created_at',
                                                                                   'end_at',
                                                                                   'plated_end_at')
    return render(request, 'my_orders.html', context={'orders': orders})