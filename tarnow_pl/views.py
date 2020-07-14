# -*- coding: utf-8 -*- 
from django.shortcuts import render
MENU_NAVIGATION = [{'link':'slider_generator', 'name':'Slider generator', 
        'describe' : 'Generowanie kodu html dla slidera na stronie głównej tarnow.pl'},
    # {'link':'/tarnow_pl', 'name':'Tarnow.pl - narzędzia', 
    #     'describe' : 'Strona główna Tarnow.pl - narzędzia'},
        ]


def main(request):
    return render(request, 'front/home.html',
        {'title': 'Tarnow.pl - narzędzia', "navigations" : MENU_NAVIGATION,
            'back': '/'})

def slider_generator(request):
    return render(request, 'tarnow_pl/slider_generator.html',
        {'title': 'Slider generator', "navigations" : MENU_NAVIGATION,
            'back': '/tarnow_pl'})
# API
from django.http import HttpResponse
import requests
def getDataFromTarnowPl(request):
    datarequest = request.GET
    url = datarequest['url']
    if(url == None):
        raise MultiValueDictKeyError    
    req = requests.get(url=url)
    return HttpResponse(req.content)