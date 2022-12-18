from django.shortcuts import render, redirect
from django.contrib import messages
from order.models import Order
from book.models import Book
from authentication.models import CustomUser
from .forms import CreateOrderForm, SearchOrderForm
import time
from rest_framework import viewsets
from .serializers import OrderSerializer, UsersOrderSerializer


def add_order(request):
    if request.method == 'POST':
        book_id = request.POST['book']
        user_id = request.POST['user']
        planed_end_at = request.POST['plated_end_at']

        book = Book.get_by_id(book_id)
        user = CustomUser.get_by_id(user_id)

        Order.create(user, book, planed_end_at)
        return redirect('all_orders')
    else:
        form = CreateOrderForm()

    context = {
        'form': form
    }
    return render(request, 'add_order.html', context)


def all_orders(request):
    if request.method == 'POST':
        form = SearchOrderForm(request.POST)
        if form.is_valid():
            user_id = request.POST['input']
            orders = Order.objects.filter(user=user_id)
            return render(request, 'all_orders.html', context={'orders': list(orders), 'form': SearchOrderForm()})
    if request.method == 'POST':
        order = Order.get_by_id(request.POST['order_id'])
        order.update(end_at=time.strftime("%Y-%m-%d %H:%M", time.gmtime(time.time())))
    orders = list(Order.objects.all())
    context = {
            'orders': orders,
            'form': SearchOrderForm()
        }
    return render(request, 'all_orders.html', context)


def my_orders(request):
    orders = Order.objects.select_related().filter(user_id=request.user.id).values('id',
                                                                                   'user__first_name',
                                                                                   'created_at',
                                                                                   'end_at',
                                                                                   'plated_end_at')
    return render(request, 'my_orders.html', context={'orders': orders})


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class UsersOrderView(viewsets.ModelViewSet):
    serializer_class = UsersOrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user_id=self.kwargs['id']).all()