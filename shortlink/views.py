from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm, CreateUrlForm
from .models import CreateURL


def index(request):
	if request.method == 'POST':
		form = CreateUrlForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data.get('url')
			try:
				url = CreateURL.objects.get(url=data)
				messages.warning(request, f'Короткая ссылка уже была создана! {url.shorted_url}')
			except:
				url = CreateURL(url=data)
				url.owner = request.user
				url.save()
				messages.success(request, f'Короткая ссылка успешно создана! {url.shorted_url}')
			return redirect('home')

	else:
		form = CreateUrlForm()
	return render(request, 'shortlink/index.html', {'form': form})


def link_redirect(request, hash):
	try:
		obj = CreateURL.objects.get(url_hash=hash)
		url = obj.url
		return redirect(url)
	except:
		messages.warning(request, f'Короткая ссылка не найдена!')
		return redirect('home')


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


def user_links(request):
	obj = CreateURL.objects.filter(owner=request.user)
	return render(request, 'shortlink/links.html', {'items': obj})
