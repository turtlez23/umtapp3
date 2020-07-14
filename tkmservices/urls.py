# -*- coding: utf-8 -*- 
from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.main, name='main'),
	path('parkometer/', views.parkometer, name='parkometer'),
	
	path('ticketvalidate/', views.ticketvalidate, name='ticketvalidate'),
	path('ticketvalidatehistory/', views.ticketvalidateHistory, name='ticketvalidatehistory'),
	
	path('printcard/', views.printCard, name='printcard'),


# nie zaimplementowane
    path('tkmservices/countcardandproposal/', views.main, name='countcardandproposal'),    
    path('tkmservices/checkblockcard/', views.main, name='tkmservices'),
    path('tkmservices/onlineproposal/', views.main, name='tkmservices'),
    path('tkmservices/print/', views.main, name='tkmservices'),
    path('tkmservices/serialprint/', views.main, name='tkmservices'),
    path('tkmservices/citycardstatistic/', views.main, name='tkmservices'),	
]