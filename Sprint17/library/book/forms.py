from django import forms
from .models import Book
from author.models import Author
from django.forms import ModelForm

class CreateBookForm(ModelForm):
    checkbox = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    def __init__(self, *args, **kwargs):
        super(CreateBookForm, self).__init__(*args, **kwargs)
        authors = [(author.id, author.name) for author in Author.objects.all()]
        self.fields['authors'] = forms.ChoiceField(choices=authors)

    class Meta:
        model = Book
        fields = ('name', 'description', 'count', 'photo')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'count': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'photo': forms.FileInput(attrs={'class': 'form-control form-control-lg'})
        }


class SearchBookForm(forms.Form):
    choices = [(0, 'Filter by'), (1, 'Author'), (2, 'Title'), (3, 'Description')]
    selector = forms.ChoiceField(choices=choices, widget=forms.Select(attrs={'class': 'form-control form-control-lg'}))
    input = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control me-2", 'type': "search", 'placeholder': "Search", 'aria-label': "Search"}))