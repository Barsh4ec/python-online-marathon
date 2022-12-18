from rest_framework import serializers
from .models import Order
from authentication.models import CustomUser
from book.models import Book

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class BookField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            'id': value.id,
            'name': value.name
        }

    def get_queryset(self):
        return Book.get_all()

    def to_internal_value(self, data):
        return Book.get_by_id(data)


class UserField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            'id': value.id,
            'username': value.first_name,
            'email': value.email
        }

    def get_queryset(self):
        return CustomUser.get_all()

    def to_internal_value(self, data):
        return CustomUser.get_by_id(data)


class UsersOrderSerializer(serializers.ModelSerializer):
    user = UserField()
    book = BookField()

    class Meta:
        model = Order
        fields = ['user', 'book', 'created_at', 'end_at', 'plated_end_at']

    def create(self, validated_data):
        return Order.create(user=validated_data['user'],
                            book=validated_data['book'],
                            plated_end_at=validated_data['plated_end_at'])
