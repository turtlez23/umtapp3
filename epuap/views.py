# -*- coding: utf-8 -*- 
from django.shortcuts import render
MENU_NAVIGATION = [
    {'link':'epuap', 'name':'Weryfikacja podpisu XML (dowód osobisty)'},
]

def main(request):
    return render(request, 'epuap/main.html', 
        {'title': 'Weryfikacja podpisu XML (dowod osobisty)',
            "navigations" : MENU_NAVIGATION, 'back':'/'})