from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm


def index(request):
	return render(request, 'shortlink/index.html')


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)

		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, 'Вы успешно зарегистрировались!')
			return redirect('home')
		else:
			messages.error(request, 'Ошибка регистрации!')

	else:
		form = UserRegisterForm()

	return render(request, 'shortlink/register.html', {'form': form})


def user_login(request):
	if request.method == 'POST':
		form = UserLoginForm(data=request.POST)

		if form.is_valid():
			user = form.get_user()
			login(request, user)
			messages.success(request, 'Вы успешно вошли!')
			return redirect('home')
		else:
			messages.error(request, 'Ошибка входа!')

	else:
		form = UserLoginForm()

	return render(request, 'shortlink/login.html', {'form': form})


def user_logout(request):
	logout(request)
	return redirect('login')