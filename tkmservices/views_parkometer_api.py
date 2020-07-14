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
def tkmGetAllParkometerDevices(request, **httpresponse_kwargs):
    """ This function gets data from versioned tkm vebservices tkmGetAllParkometerDevices_.
        Actual version is define in settings.py
        Downloaded data is list of parkometer devices

    Arguments:
        request {Http.request} -- http request
        **httpresponse_kwargs -- **httpresponse_kwargs    
    
    Returns: http json response
    """
    permisions = settings.TKMSERVICES_PARKOMETER_PERMISIONS
    if not isAutorized(request.user, permisions):
        return HttpResponse('Unauthorized', status=401)

    url = settings.TKM_WEBSERVICE_ADDRESS +'tkmGetAllParkometerDevices_'+ settings.TKM_WEBSERVICE_VERSION
    params = {
        "queryParams":[{
            "name": "key",
            "value": settings.TKM_WEBSERVICES_AUTH_KEY}
        ]
    }
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    req = requests.post(url=url, data=json.dumps(params), headers=headers, auth=(settings.TKM_WEBSERVICE_USER_LOGIN, settings.TKM_WEBSERVICE_USER_PASS))

    return HttpResponse(req.content, content_type='application/json')

@login_required(login_url='/loginform/')
def tkmParkometerTransactionsOneDevices(request, **httpresponse_kwargs):
    """ This function gets data from versioned tkm vebservices tkmParkometerTransactions_TypeDevicename_.
        Downloaded data is list of parkometer transactions for specific device
        Actual version is define in settings.py
    Arguments:
        request {Http.request} -- http request
        **httpresponse_kwargs -- **httpresponse_kwargs
    
    Returns: http json response
    """
    permisions = settings.TKMSERVICES_PARKOMETER_PERMISIONS
    if not isAutorized(request.user, permisions):
        return HttpResponse('Unauthorized', status=401)

    datarequest = request.GET
    startdate = datarequest['startdate']
    enddate = datarequest['enddate']    
    type = datarequest['type']    
    deviceName = datarequest['devicename']    
    if(startdate == None or enddate == None or type == None or deviceName == None):
        raise MultiValueDictKeyError
    url = settings.TKM_WEBSERVICE_ADDRESS +'tkmParkometerTransactions_TypeDevicename_'+ settings.TKM_WEBSERVICE_VERSION
    params = {
        "queryParams":[{
            "name": "startdate",
            # "value": "2019-01-01"},{
            "value": startdate},{
            "name": "enddate",
            # "value": "2020-01-01"},{
            "value": enddate},{
            "name": "type",
            "value": type},{
            "name": "devicename",
            "value": deviceName},{
            "name": "key",
            "value": settings.TKM_WEBSERVICES_AUTH_KEY}
        ]
    }
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    req = requests.post(url=url, data=json.dumps(params), headers=headers, auth=(settings.TKM_WEBSERVICE_USER_LOGIN, settings.TKM_WEBSERVICE_USER_PASS))

    return HttpResponse(req.content, content_type='application/json')

@login_required(login_url='/loginform/')
def tkmParkometerTransactionsCountOneDevices(request, **httpresponse_kwargs):
    """ This function gets data from versioned tkm vebservices tkmParkometerTransactionsCount_TypeDevicename_.
        Downloaded data is statistics of parkometer transactions for specific device
        Actual version is define in settings.py
    Arguments:
        request {Http.request} -- http request
        **httpresponse_kwargs -- **httpresponse_kwargs
    
    Returns: http json response
    """
    permisions = settings.TKMSERVICES_PARKOMETER_PERMISIONS
    if not isAutorized(request.user, permisions):
        return HttpResponse('Unauthorized', status=401)

    datarequest = request.GET
    startdate = datarequest['startdate']
    enddate = datarequest['enddate']    
    type = datarequest['type']    
    deviceName = datarequest['devicename']    
    if(startdate == None or enddate == None or type == None or deviceName == None):
        raise MultiValueDictKeyError
    url = settings.TKM_WEBSERVICE_ADDRESS +'tkmParkometerTransactionsCount_TypeDevicename_'+ settings.TKM_WEBSERVICE_VERSION
    params = {
        "queryParams":[{
            "name": "startdate",
            # "value": "2019-01-01"},{
            "value": startdate},{
            "name": "enddate",
            # "value": "2020-01-01"},{
            "value": enddate},{
            "name": "type",
            "value": type},{
            "name": "devicename",
            "value": deviceName},{
            "name": "key",
            "value": settings.TKM_WEBSERVICES_AUTH_KEY}
        ]
    }
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    req = requests.post(url=url, data=json.dumps(params), headers=headers, auth=(settings.TKM_WEBSERVICE_USER_LOGIN, settings.TKM_WEBSERVICE_USER_PASS))

    return HttpResponse(req.content, content_type='application/json')

@login_required(login_url='/loginform/')
def tkmParkometerTransactionsCountAllDevices(request, **httpresponse_kwargs):
    """ This function gets data from versioned tkm vebservices tkmParkometerTransactionsCountAllDevices_.
        Downloaded data is statistics of parkometer transactions for all devices
        Actual version is define in settings.py
    Arguments:
        request {Http.request} -- http request
        **httpresponse_kwargs -- **httpresponse_kwargs
    
    Returns: http json response
    """
    permisions = settings.TKMSERVICES_PARKOMETER_PERMISIONS
    if not isAutorized(request.user, permisions):
        return HttpResponse('Unauthorized', status=401)
        
    datarequest = request.GET
    startdate = datarequest['startdate']
    enddate = datarequest['enddate']    
    if(startdate == None or  enddate == None):
        raise MultiValueDictKeyError
    url = settings.TKM_WEBSERVICE_ADDRESS +'tkmParkometerTransactionsCountAllDevices_'+ settings.TKM_WEBSERVICE_VERSION
    params = {
        "queryParams":[{
            "name": "startdate",
            # "value": "2019-01-01"},{
            "value": startdate},{
            "name": "enddate",
            # "value": "2020-01-01"},{
            "value": enddate},{
            "name": "key",
            "value": settings.TKM_WEBSERVICES_AUTH_KEY}
        ]
    }
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    req = requests.post(url=url, data=json.dumps(params), headers=headers, auth=(settings.TKM_WEBSERVICE_USER_LOGIN, settings.TKM_WEBSERVICE_USER_PASS))

    return HttpResponse(req.content, content_type='application/json')
    
@login_required(login_url='/loginform/')
def tkmParkometerTransactionsCountAll(request, **httpresponse_kwargs):
    """ This function gets data from versioned tkm vebservices tkmParkometerTransactionsCountAll_.
        Downloaded data is statistics of all parkometer transactions
        Actual version is define in settings.py
    Arguments:
        request {Http.request} -- http request
        **httpresponse_kwargs -- **httpresponse_kwargs
    
    Returns: http json response
    """
    permisions = settings.TKMSERVICES_PARKOMETER_PERMISIONS
    if not isAutorized(request.user, permisions):
        return HttpResponse('Unauthorized', status=401)
        
    datarequest = request.GET
    startdate = datarequest['startdate']
    enddate = datarequest['enddate']    
    if(startdate == None or  enddate == None):
        raise MultiValueDictKeyError
    url = settings.TKM_WEBSERVICE_ADDRESS +'tkmParkometerTransactionsCountAll_'+ settings.TKM_WEBSERVICE_VERSION
    params = {
        "queryParams":[{
            "name": "startdate",
            # "value": "2019-01-01"},{
            "value": startdate},{
            "name": "enddate",
            # "value": "2020-01-01"},{
            "value": enddate},{
            "name": "key",
            "value": settings.TKM_WEBSERVICES_AUTH_KEY}
        ]
    }    
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    req = requests.post(url=url, data=json.dumps(params), headers=headers, auth=(settings.TKM_WEBSERVICE_USER_LOGIN, settings.TKM_WEBSERVICE_USER_PASS))
    return HttpResponse(req.content, content_type='application/json')
