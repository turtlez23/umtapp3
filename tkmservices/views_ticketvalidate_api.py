# -*- coding: utf-8 -*- 
import io
import os
import sys

import json
import requests

from django.conf import settings
from django.shortcuts import render, redirect 

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError

from .views import isAutorized, castParamToBoolean, getVariantFromBooleanParam


@login_required(login_url='/loginform/')
def tkmTicketValidateHistory(request):
    permisions = settings.TKMSERVICES_TICKETVALIDATE_PERMISIONS
    if not isAutorized(request.user, permisions):
        return HttpResponse('Unauthorized', status=401)

    datarequest = request.GET
    duplicate = datarequest['duplicate']
    card = datarequest['card']

    startdate = datarequest['startdate']
    enddate = datarequest['enddate'] 
    if(duplicate == None or  card == None or
        startdate == None or  enddate == None):
        raise MultiValueDictKeyError
    webserviceName = ''
    #cast to boolean
    duplicate = castParamToBoolean(duplicate)
    if(duplicate):
        webserviceName = 'tkmTicketValidateHistoryDpl_'
    else:
        webserviceName = 'tkmTicketValidateHistory_'
    url = settings.TKM_WEBSERVICE_ADDRESS + webserviceName + settings.TKM_WEBSERVICE_VERSION
    params = {
        "queryParams":[{
            "name": "card",
            "value": str(card)},{
            "name": "startdate",
            "value": startdate},{
            "name": "enddate",
            "value": enddate},{
            "name": "key",
            "value": settings.TKM_WEBSERVICES_AUTH_KEY}
        ]
    }
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    req = requests.post(url=url, data=json.dumps(params), headers=headers, auth=(settings.TKM_WEBSERVICE_USER_LOGIN, settings.TKM_WEBSERVICE_USER_PASS))

    return HttpResponse(req.content, content_type='application/json')

@login_required(login_url='/loginform/')
def tkmMyselfFellowCount(request):
    permisions = settings.TKMSERVICES_TICKETVALIDATE_PERMISIONS
    if not isAutorized(request.user, permisions):
        return HttpResponse('Unauthorized', status=401)

    datarequest = request.GET
    duplicate = datarequest['duplicate']
    transfered = datarequest['transfered']

    startdate = datarequest['startdate']
    enddate = datarequest['enddate']    
    if(duplicate == None or  transfered == None or
        startdate == None or  enddate == None):
        raise MultiValueDictKeyError
    webserviceName = ''
    #cast to boolean
    duplicate = castParamToBoolean(duplicate)
    transfered = castParamToBoolean(transfered)
    if(duplicate):
        webserviceName = 'tkmCountTicket_BusstopMyselfFellowDpl_'
    else:
        webserviceName = 'tkmCountTicket_BusstopMyselfFellow_'
    url = settings.TKM_WEBSERVICE_ADDRESS + webserviceName + settings.TKM_WEBSERVICE_VERSION
    params = {
        "queryParams":[{
            "name": "transfered",
            "value": str(transfered)},{
            "name": "startdate",
            "value": startdate},{
            "name": "enddate",
            "value": enddate},{
            "name": "key",
            "value": settings.TKM_WEBSERVICES_AUTH_KEY}
        ]
    }
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    req = requests.post(url=url, data=json.dumps(params), headers=headers, auth=(settings.TKM_WEBSERVICE_USER_LOGIN, settings.TKM_WEBSERVICE_USER_PASS))

    return HttpResponse(req.content, content_type='application/json')

@login_required(login_url='/loginform/')
def tkmMyselfFellowWithVariantCount(request):
    permisions = settings.TKMSERVICES_TICKETVALIDATE_PERMISIONS
    if not isAutorized(request.user, permisions):
        return HttpResponse('Unauthorized', status=401)

    datarequest = request.GET
    duplicate = datarequest['duplicate']
    transfered = datarequest['transfered']
    duplicate = datarequest['duplicate']
    variant = datarequest['variant']

    startdate = datarequest['startdate']
    enddate = datarequest['enddate']    
    if(variant == None or duplicate == None or  transfered == None or
        startdate == None or  enddate == None):
        raise MultiValueDictKeyError
    webserviceName = ''
    #cast to boolean
    duplicate = castParamToBoolean(duplicate)
    transfered = castParamToBoolean(transfered)
    variant = getVariantFromBooleanParam(variant)
    if(duplicate):
        webserviceName = 'tkmCountTicket_V_BusstopMyselfFellowDpl_'
    else:
        webserviceName = 'tkmCountTicket_V_BusstopMyselfFellow_'
    url = settings.TKM_WEBSERVICE_ADDRESS + webserviceName + settings.TKM_WEBSERVICE_VERSION
    params = {
        "queryParams":[{
            "name": "transfered",
            "value": str(transfered)},{
            "name": "variant",
            "value": str(variant)},{
            "name": "startdate",
            "value": startdate},{
            "name": "enddate",
            "value": enddate},{
            "name": "key",
            "value": settings.TKM_WEBSERVICES_AUTH_KEY}
        ]
    }
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    req = requests.post(url=url, data=json.dumps(params), headers=headers, auth=(settings.TKM_WEBSERVICE_USER_LOGIN, settings.TKM_WEBSERVICE_USER_PASS))

    return HttpResponse(req.content, content_type='application/json')
    # return HttpResponse(
    #     "url "+ url +
    #     " duplicate:"+str(duplicate) + 
    #     " transfered:"+str(transfered) + 
    #     " variant:"+str(variant) + 
    #     " startdate:"+startdate +
    #     " enddate:"+enddate, 
    #     content_type='application/json')

@login_required(login_url='/loginform/')
def tkmLineSocialGroupFromClientTableCount(request):
    permisions = settings.TKMSERVICES_TICKETVALIDATE_PERMISIONS
    if not isAutorized(request.user, permisions):
        return HttpResponse('Unauthorized', status=401)
        
    datarequest = request.GET
    duplicate = datarequest['duplicate']
    transfered = datarequest['transfered']
    duplicate = datarequest['duplicate']
    variant = datarequest['variant']

    startdate = datarequest['startdate']
    enddate = datarequest['enddate']    
    if(variant == None or duplicate == None or  transfered == None or
        startdate == None or  enddate == None):
        raise MultiValueDictKeyError
    webserviceName = ''
    #cast to boolean
    duplicate = castParamToBoolean(duplicate)
    transfered = castParamToBoolean(transfered)
    variant = getVariantFromBooleanParam(variant)
    if(duplicate):
        webserviceName = 'tkmCountTicket_SG_BusstopSocialgroupLineMyselfFellowDpl_'
    else:
        webserviceName = 'tkmCountTicket_SG_BusstopSocialgroupLineMyselfFellow_'
    url = settings.TKM_WEBSERVICE_ADDRESS + webserviceName + settings.TKM_WEBSERVICE_VERSION
    params = {
        "queryParams":[{
            "name": "transfered",
            "value": str(transfered)},{
            "name": "variant",
            "value": str(variant)},{
            "name": "startdate",
            "value": startdate},{
            "name": "enddate",
            "value": enddate},{
            "name": "key",
            "value": settings.TKM_WEBSERVICES_AUTH_KEY}
        ]
    }
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    req = requests.post(url=url, data=json.dumps(params), headers=headers, auth=(settings.TKM_WEBSERVICE_USER_LOGIN, settings.TKM_WEBSERVICE_USER_PASS))

    return HttpResponse(req.content, content_type='application/json')
 
@login_required(login_url='/loginform/')
def tkmLineSocialGroupFromTpTableCount(request):
    permisions = settings.TKMSERVICES_TICKETVALIDATE_PERMISIONS
    if not isAutorized(request.user, permisions):
        return HttpResponse('Unauthorized', status=401)
        
    datarequest = request.GET
    duplicate = datarequest['duplicate']
    transfered = datarequest['transfered']
    duplicate = datarequest['duplicate']
    variant = datarequest['variant']

    startdate = datarequest['startdate']
    enddate = datarequest['enddate']    
    if(variant == None or duplicate == None or  transfered == None or
        startdate == None or  enddate == None):
        raise MultiValueDictKeyError
    webserviceName = ''
    #cast to boolean
    duplicate = castParamToBoolean(duplicate)
    transfered = castParamToBoolean(transfered)
    variant = getVariantFromBooleanParam(variant)
    if(duplicate):
        webserviceName = 'tkmCountTicket_BusstopSocialgroupLineMyselfFellowDpl_'
    else:
        webserviceName = 'tkmCountTicket_BusstopSocialgroupLineMyselfFellow_'
    url = settings.TKM_WEBSERVICE_ADDRESS + webserviceName + settings.TKM_WEBSERVICE_VERSION
    params = {
        "queryParams":[{
            "name": "transfered",
            "value": str(transfered)},{
            "name": "variant",
            "value": str(variant)},{
            "name": "startdate",
            "value": startdate},{
            "name": "enddate",
            "value": enddate},{
            "name": "key",
            "value": settings.TKM_WEBSERVICES_AUTH_KEY}
        ]
    }
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    req = requests.post(url=url, data=json.dumps(params), headers=headers, auth=(settings.TKM_WEBSERVICE_USER_LOGIN, settings.TKM_WEBSERVICE_USER_PASS))

    return HttpResponse(req.content, content_type='application/json')
