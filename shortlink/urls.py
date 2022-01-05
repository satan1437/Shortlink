from django.urls import path, re_path
from .views import *

urlpatterns = [
	path('', index, name='home'),
	path('login/', user_login, name='login'),
	path('logout/', user_logout, name='logout'),
	path('links/', user_links, name='links'),
	path('register/', register, name='register'),
	re_path(r'^(?P<hash>.+)$', link_redirect),
]
