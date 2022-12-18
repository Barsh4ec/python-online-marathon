from django.contrib import admin
from .models import Book
from author.models import Author
from django.utils.safestring import mark_safe


class MemberShip(admin.TabularInline):
    model = Author.books.through
    def has_add_permission(self, request, obj = None):
        return not bool(obj)

    def has_change_permission(self, request, obj=None):
        return not bool(obj)

    def has_delete_permission(self, request, obj=None):
        return not bool(obj)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'count', 'get_author', 'get_photo')
    list_filter = ('id', 'name', 'authors')

    def get_author(self, obj):
        return [i.surname for i in obj.authors.all()]

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=75">')

    get_photo.short_description = 'Фото'
    inlines = [MemberShip]