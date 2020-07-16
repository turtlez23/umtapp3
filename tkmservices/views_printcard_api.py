# -*- coding: utf-8 -*-
import io
import os
import sys

import json
import requests

from django.conf import settings
from django.shortcuts import render, redirect 

from django.http import HttpResponse
from django.http import FileResponse

from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError

from .views import isAutorized, castParamToBoolean, getVariantFromBooleanParam, getFilesList, getResponseFromTkmWebServices

import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab import platypus
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import logging
logger = logging.getLogger(__name__)

# Print settings
WIDTH = 86*mm
HEIGHT = 54*mm
TEXT_X = 10*mm
TEXT_Y = 42*mm
FONT_SIZE = 10
FONT_H = 4*mm
PHOTO_X = 64*mm
PHOTO_Y = 13*mm
PHOTO_W = 13*mm
PHOTO_H = 17*mm
FOREIGNER_ID_LENGTH = len('2000-05-27')

def tkmGetCustomerFormData(startDate, endDate, variant, online):          
    # "CLOSED"        
    # "TO_PERSONALIZE"
    # "REJECTED"      
    # "PERSONALIZED"  
    # "NEW"           
    url = settings.TKM_WEBSERVICE_ADDRESS + 'tkmGetCustomerRequest_to_personalize_' + settings.TKM_WEBSERVICE_VERSION
    params = {
        "queryParams":[{
            "name": "online",
            "value": str(online)},{
            "name": "variant",
            "value": str(variant)},{
            "name": "startdate",
            "value": startDate},{
            "name": "enddate",
            "value": endDate},{
            "name": "key",
            "value": settings.TKM_WEBSERVICES_AUTH_KEY}
        ]
    }
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    req = requests.post(url=url, data=json.dumps(params), headers=headers, auth=(settings.TKM_WEBSERVICE_USER_LOGIN, settings.TKM_WEBSERVICE_USER_PASS))
    return getResponseFromTkmWebServices(json.loads(req.content))
    # reqJsonTMP = json.loads(req.content)
    # reqJson ={}
    # reqJson = reqJsonTMP['message'][0]
    # reqJson['response'] = json.loads(reqJsonTMP['message'][0].get('response', '[]'))   
    # return reqJson

@login_required(login_url='/loginform/')
def tkmGetPhotoList(request):
    permisions = settings.TKMSERVICES_PRINTCARD_PERMISIONS
    if isAutorized(request.user, permisions):
        photos = getFilesList(settings.PHOTO_DIR)
        return HttpResponse([photos], content_type='application/json')
    return HttpResponse('Brak uprawnień:'+ ', '.join(permisions), content_type='application/json')

@login_required(login_url='/loginform/')
def tkmPdfExport(request):    
    permisions = settings.TKMSERVICES_PRINTCARD_PERMISIONS
    if isAutorized(request.user, permisions):
        datarequest = request.GET
        name = datarequest['name']
        surname = datarequest['surname']
        id = datarequest['id']
        text = datarequest.get('text', '')
        if(name == None or surname == None or id == None):
            raise MultiValueDictKeyError
            
        title = name +'_'+ surname +'.pdf'
        bufferedPdf = None
        try:
            bufferedPdf = pdfExport(name, surname, id, title, text)
            return FileResponse(bufferedPdf, as_attachment=True, filename=title+'.pdf')
        except:        
            logger.error(sys.exc_info())
            return redirect('/tkmservices/printcard/?name='+str(name)+
                '&surname='+str(surname)+'&id='+str(id)+'&text='+
                    str(text)+'&error=BŁĄD EKSPORTU - SPRAWDŹ ZDJĘCIE !! :'+str(id))
    return render(request, 'front/loginform.html', {'text':'Wymagane uprawnienia: '+ ', '.join(permisions), 'back': '/tkmservices'})

@login_required(login_url='/loginform/')
def tkmPdfMultipleExport(request):
    permisions = settings.TKMSERVICES_PRINTCARD_PERMISIONS    
    if isAutorized(request.user, permisions):
        datarequest = request.GET
        startDate = datarequest['startdate']
        endDate = datarequest['enddate']
        variant = getVariantFromBooleanParam(datarequest['variant'])
        online = castParamToBoolean(datarequest['online'])
        if(startDate == None or endDate == None or variant == None or online == None):
            raise MultiValueDictKeyError
        data = tkmGetCustomerFormData(startDate, endDate, variant, online)

        title = 'Eksport '+ startDate +'-'+ endDate +', wariant '+ variant +', czy online '+ str(online) +'.pdf'
        bufferedPdf = None
        try:
            bufferedPdf = pdfMultiPagesExport(title, data)
            return FileResponse(bufferedPdf, as_attachment=True, filename=title+'.pdf')
        except:
            logger.error(sys.exc_info())
            return redirect('/tkmservices/printcard/?error=BŁĄD EKSPORTU - SPRAWDŹ ZDJĘCIA !! :'+ startDate +'-'+ endDate)
        return render(request, 'front/loginform.html', {'text':'Wymagane uprawnienia: '+ ', '.join(permisions), 'back': '/tkmservices'})

def getPhotoName(id):
    if not id:
        return 'błąd id'
    if id.find('.jpg') == -1:
        id += '.jpg'
    return settings.PHOTO_DIR  + id

def generateOnePagePdf(p, data, id):
    p.setFont("Arial-bold", FONT_SIZE)
    p.drawString(TEXT_X, TEXT_Y, data['name'].upper()+'  '+data['surname'].upper())
    p.drawString(TEXT_X, TEXT_Y-FONT_H, data['text'].upper())
    p.drawInlineImage(getPhotoName(id), PHOTO_X, PHOTO_Y, PHOTO_W, PHOTO_H)
    p.showPage()

def pdfExport(name, surname, id, title, text):
    # register arial bond font
    if settings.FONTS:
        pdfmetrics.registerFont(TTFont('Arial-bold', settings.FONTS+'arial-bold.ttf'))
    # Standard const params
    bufferedPdf = io.BytesIO()
    p = canvas.Canvas(bufferedPdf)
    p.setTitle(title)
    data = {'name': name, 'surname': surname, 'id': id, 'text': ''}
    generateOnePagePdf(p, data, id)
    p.save()
    bufferedPdf.seek(0)
    return bufferedPdf

def pdfMultiPagesExport(title, data):
    if settings.FONTS:
        pdfmetrics.registerFont(TTFont('Arial-bold', settings.FONTS+'arial-bold.ttf'))
    lostPhotos = []
    bufferedPdf = io.BytesIO()    
    p = canvas.Canvas(bufferedPdf)
    p.setPageSize((WIDTH, HEIGHT))
    p.setTitle(title)
    for d in data['response']:
        fileName = None
        id = d['id']
        if id:
            fileName = getPhotoName(id)
        elif d['birthdate'] :
            id = str(d['birthdate'])[0:FOREIGNER_ID_LENGTH]+ '_' +d['name'][0:1].upper()
            fileName = getPhotoName(id)
        if os.path.exists(fileName):
            generateOnePagePdf(p, d, id)
        else:
            lostPhotos.append(id +'.jpg - '+ d['name'] +' '+ d['surname'])
    p.setPageSize((210*mm, 297*mm))
    x = TEXT_X
    y = 290*mm
    lostPhotos.append('Ilość: '+ str(len(lostPhotos)))
    for photo in lostPhotos:
        p.setFont("Arial-bold", FONT_SIZE)
        p.drawString(x, y, photo)
        y = y-FONT_H
    p.showPage()
    p.save()
    bufferedPdf.seek(0)
    return bufferedPdf