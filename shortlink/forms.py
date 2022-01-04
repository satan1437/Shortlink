from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
	username = forms.CharField(
		label='',
		help_text='Только буквы, цифры и символы @/./+/-/_.',
		widget=forms.TextInput(attrs={
			'class': 'form-control',
			'autocomplete': 'off',
			'placeholder': 'Имя пользователя',
		}))
	password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
		'class': 'form-control',
		'placeholder': 'Пароль',
	}))
	password2 = forms.CharField(
		label='',
		help_text='Ваш пароль должен содержать как минимум 8 символов.',
		widget=forms.PasswordInput(attrs={
			'class': 'form-control',
			'placeholder': 'Повтор пароля'
		}))

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
	username = forms.CharField(label='', widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Имя пользователя',
	}))
	password = forms.CharField(label='', widget=forms.PasswordInput(attrs={
		'class': 'form-control',
		'placeholder': 'Пароль',
	}))
