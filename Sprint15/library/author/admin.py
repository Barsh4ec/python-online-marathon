from django.contrib import admin
from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'patronymic', 'surname', 'get_books')


    fieldsets = (
        (None, {'fields': ('name', 'patronymic', 'surname',)}),
        ('Books', {'fields': ('books',)}),
    )

    def get_books(self, obj):
        return [i.name for i in obj.books.all()]

    list_filter = ('name', 'surname', 'patronymic', ('books__name', admin.EmptyFieldListFilter))