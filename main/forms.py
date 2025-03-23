from django import forms
from django.contrib.auth.models import User
from .models import *
from django.forms import TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["name", "text"]

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш комментарий'
            })
        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['author', 'popularity', 'category', 'img1', 'img2', 'title', 'description']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя автора'}),
            'popularity': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'img1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'img2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Введите описание новости'}),
        }

