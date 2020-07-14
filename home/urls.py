# -*- coding: utf-8 -*- 
from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('accounts/profile/', views.home, name='accounts_profile'),
	
    path('loginform/', views.loginForm, name='loginform'),
	
    path('login/', views.logIn, name='login'),
    path('logout/', views.logOut, name='logout'),
]