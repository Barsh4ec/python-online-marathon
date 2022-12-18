from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class UserRegisterForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'first_name', 'middle_name', 'last_name', 'role')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'role': forms.Select(attrs={'class': 'form-control form-control-lg'})
        }


class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))


class SearchUserForm(forms.Form):
    input = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control me-2", 'type': "search", 'placeholder': "Search", 'aria-label': "Search"}))
