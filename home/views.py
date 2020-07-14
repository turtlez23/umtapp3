# -*- coding: utf-8 -*- 
from django.shortcuts import render, redirect
MENU_NAVIGATION = [
    {'link':'tarnow_pl', 'name':'Tarnow_pl - narzędzia', 
        'describe' : 'Narzędzia dodatkowe do edycji strony tarnow.pl'},
    {'link':'tkmservices', 'name':'Tarnowska Karta Miejska - narzędzia', 
        'describe' : 'Narzędzia dodatkowe do Systemu Tarnowskiej Karty Miejskiej'},
    {'link':'epuap', 'name':'Weryfikacja podpisu XML (dowod osobisty)', 
        'describe' : 'Weryfikowanie podpisu załączonego w postaci pliku xml'},
    # {'link':'xml-sign-werify', 'name':'Weryfikacja podpisu XML (dowod osobisty)'},
]

import logging
logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'front/home.html',
        {'title': 'Aplikacja UMT', "navigations" : MENU_NAVIGATION,
            'back': ''})
			
			
# Autenticate view
from django.contrib.auth import authenticate, login, logout

def loginForm(request):
    return render(request, 'front/loginform.html', 
        {'title' : 'LOGOWANIE', 'navigations' : MENU_NAVIGATION, 'back' : '/', 'redirectpage' : request.META['HTTP_REFERER']})

# Autenticate API
def logOut(request):
    logout(request)
    logger.info('UŻYTKOWNIK: "'+ request.user.username +'" zostal wylogowany z systemu')
    return redirect('/')

def logIn(request):
    datarequest = request.POST    
    userName  = datarequest['username']
    password   = datarequest['password']
    redirectPage   = datarequest['redirectpage']
    if(not redirectPage):
        redirectPage = '/'
    user = authenticate(request, username=userName, password=password)
    if user is not None:
        login(request, user)
        logger.info('UŻYTKOWNIK: "'+ datarequest['username'] +'" zostal zalogowany do systemu')
        return redirect(redirectPage)
    else:
        logger.info('UŻYTKOWNIK: "'+ datarequest['username'] +'"- blędne dane logowania')
        return redirect('/error/?message=Aby się zalogować musisz podać poprawny login lub hasło lub posiadać uprawnienia do tego elementu.')


# def user_page(request):
#     return render(request, 'front/home.html', {'title': 'Aplikacja UMT', "navigations" : MENU_NAVIGATION})