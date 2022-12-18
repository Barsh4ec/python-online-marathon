from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user', 'get_book', 'created_at', 'end_at', 'plated_end_at')
    list_filter = ('id', 'user', 'book')

    def get_user(self, obj):
        return obj.user.email

    def get_book(self, obj):
        return obj.book.name

admin.site.register(Order, OrderAdmin)