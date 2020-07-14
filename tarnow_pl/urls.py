# -*- coding: utf-8 -*- 
from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.main, name='main'),
	path('slider_generator/', views.slider_generator, name='slider_generator'),	
]