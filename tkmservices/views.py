# -*- coding: utf-8 -*- 
import os
import json
import requests

from django.conf import settings
from django.shortcuts import render, redirect 

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError

#List of all links to navigation menu
MENU_NAVIGATION = [
    {'link':'parkometer', 'name':'Rozliczenia parkometry', 
        'describe':'Rozliczenia transakcji miesięcznych w parkomatach - Targowiska Miejskie'},
    {'link':'ticketvalidate', 'name':'Statystyka skasowań biletów odległościowych',
        'describe':'Rozliczenia transakcji miesięcznych w kasownikach autobusowych - Zarząd Dróg i Komunikacji Miejskiej'},
    {'link':'ticketvalidatehistory', 'name':'Historia skasowań', 'describe':'Historia skasowań dla podanej karty'},
    {'link':'printcard', 'name':'Drukowanie TKM', 'describe' :'Drukowanie kart miejskich'},
    {'link':'countcardandproposal', 'name':'Liczba kart i wniosków',
        'describe':'W budowie...'},
    {'link':'checkblockcard', 'name':'Sprawdzenie zablokowanej karty',
        'describe':'W budowie...'},
    {'link':'onlineproposal', 'name':'Wnioski online',
        'describe':'W budowie...'},
    {'link':'citycardstatistic', 'name':'Statystyka karty miejskiej',
        'describe':'W budowie...'},
]
#def isAuthenticated(user):    
#    if(user and user.is_authenticated()):
#        return True
#    return False
#
#def isAutorized(user, permisions):   
#    if(isAuthenticated(user)):
#        groups = user.groups
#        if (groups and groups.filter(name__in=permisions).exists()):
#            return True
#    return False
#def isAutorized(user, permisions):
#	checked = False
#	for perm in permisions:
#		checked *= user.has_perm(perm)
#	return checked

def isAutorized(user, permisions):
	for perm in permisions:
		if(user.has_perm(perm)):
			return True
	return False

def castParamToBoolean(param):
    if(param == 'true' or param == 'on' or param == 'True' or param == 1 or param == '1'):
        return True
    return False
def getVariantFromBooleanParam(param):
    if(castParamToBoolean(param)):
        return 'PREMIUM_CARD'
    return 'STANDARD_CARD'

def getFilesList(path):
    listDir = os.listdir(path)
    return listDir
    # return [f for f in listdir(path) if isfile(join(path, f))]

@login_required(login_url='/loginform/')
def main(request):
	""" Main view in home application, then is rendered main page and main navigation

	Arguments:
		request {Http.request} -- http request

	Returns: rendered view
	"""
	return render(request, 'front/home.html',
		{'title' : 'Tarnowska Karta Miejska - narzędzia',
			'navigations' : MENU_NAVIGATION, 'back': '/'})

@login_required(login_url='/loginform/')
def parkometer(request):
    """ Main view for parkometer application , then is rendered main page and main navigation

    Arguments:
        request {Http.request} -- http request
    
    Returns: rendered view
    """
    backUrl = '/tkmservices'
    permisions = settings.TKMSERVICES_PARKOMETER_PERMISIONS
    if isAutorized(request.user, permisions):
        return render(request, 'tkmservices/parkometer/main.html',
            {'title': 'Rozliczenia parkometry',
                "navigations" : MENU_NAVIGATION, 'back': backUrl})
    return render(request, 'front/loginform.html', {'text':'Wymagane uprawnienia: '+ ', '.join(permisions), 'back': backUrl})

@login_required(login_url='/loginform/')
def ticketvalidate(request):
    """ Main view for ticket validate application , then is rendered main page and main navigation

    Arguments:
        request {Http.request} -- http request
    
    Returns: rendered view
    """
    permisions = settings.TKMSERVICES_TICKETVALIDATE_PERMISIONS
    backUrl = '/tkmservices'
    if isAutorized(request.user, permisions):
        return render(request, 'tkmservices/ticketvalidate/main.html', 
                {'title': 'Rozliczenia skasowania biletów',
                    "navigations" : MENU_NAVIGATION, 'back': backUrl})            
    return render(request, 'front/loginform.html', {'text':'Wymagane uprawnienia: '+ ', '.join(permisions), 'back': backUrl})

@login_required(login_url='/loginform/')
def ticketvalidateHistory(request):
    """ Main view for ticket validate application , then is rendered main page and main navigation

    Arguments:
        request {Http.request} -- http request
    
    Returns: rendered view
    """
    permisions = settings.TKMSERVICES_TICKETVALIDATE_PERMISIONS
    backUrl = '/tkmservices'
    if isAutorized(request.user, permisions):
        return render(request, 'tkmservices/ticketvalidate/history.html', 
                {'title': 'Historia skasowań',
                    "navigations" : MENU_NAVIGATION, 'back': backUrl})            
    return render(request, 'front/loginform.html', {'text':'Wymagane uprawnienia: '+ ', '.join(permisions), 'back': backUrl})

@login_required(login_url='/loginform/') 
def printCard(request):    
    permisions = settings.TKMSERVICES_PRINTCARD_PERMISIONS
    backUrl = '/tkmservices'
    if isAutorized(request.user, permisions):
        # person = {'name': '', 'surname':'', 'id':'', 'text':''}
        person = {}
        error =''
        datarequest = request.GET
        person['name'] = datarequest.get('name', '')
        person['surname'] = datarequest.get('surname', '')
        person['id'] = datarequest.get('id', '')
        person['text'] = datarequest.get('text', '')
        error = datarequest.get('error', '')     
   
        photos = getFilesList(settings.PHOTO_DIR)

        return render(request, 'tkmservices/printcard/main.html', 
                {'title': 'Eksport do PDF',
                    "navigations" : MENU_NAVIGATION, 'back': backUrl, 'error': error, 'person' : person, 'photos' :photos})            
    return render(request, 'front/loginform.html', {'text':'Wymagane uprawnienia: '+ ', '.join(permisions), 'back': backUrl})