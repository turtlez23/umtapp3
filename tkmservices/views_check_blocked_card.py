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

from .views import getResponseFromTkmWebServices, isAutorized, castParamToBoolean, getVariantFromBooleanParam

import logging
logger = logging.getLogger(__name__)


def checkEpurseTransfer(cardNumber, startDate, endDate):
    url = settings.TKM_WEBSERVICE_ADDRESS +  'tkmGetCustomerRequest_count_registration_and_duplicate_type_' + settings.TKM_WEBSERVICE_VERSION
    params = {
        "queryParams":[{
            "name": "cardnumber",
            "value": cardNumber},{
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