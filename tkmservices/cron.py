from datetime import datetime

from django.conf import settings

from .views import checkOnlineCustomerRequest, sendEmail, countBillingWeekDuplicateAndRegistrationCustomerRequest

import logging
logger = logging.getLogger(__name__)

def testCron():
    strTest = '###################### test CRON ######################'
    print(strTest)
    logger.error(strTest)

def sendMailWithOnlineCustomRequests():
    reqJson = checkOnlineCustomerRequest()
    objs = reqJson['response']
    count = str(len(objs))    
    now = datetime.now()
    current_date = now.strftime("%d-%m-%Y")
    fromAddress = settings.EMAIL_FROM_ADDRESS
    title = 'Ilość wniosków online na dzień '+ current_date
    html_message = '<h1>'+ title +':</h1><h2>'+ count +'</h2>'
    userList = settings.ONLINE_CUSTOM_REQUEST_MAIL_LIST
    if not count:
        html_message += '<h2>BRAK WNIOSKÓW ONLINE NA DZIEŃ: '+ current_date +'</h2>'
    else:
        for obj in objs:
            html_message += '<p>'+ obj['id'] +'</p>'
    
    sendStatus = sendEmail(title, fromAddress, userList, html_message)
    if sendStatus:
        logger.info('WYSLANO EMAIL: Liczba['+ str(sendStatus) +'], OD: '+ fromAddress +', DO: '+ ', '.join(userList) +',Tresc: '+ html_message)
    else:
        logger.error('NIE WYSLANO EMAIL: OD: '+ fromAddress +', DO: '+ ', '.join(userList) +',Tresc: '+ html_message)
    return reqJson

def sendmailWithCountBillingWeekDuplicateAndRegistrationCustomerRequest():
    reqJson = countBillingWeekDuplicateAndRegistrationCustomerRequest()
    count = str(reqJson['response'][0]['number'])
    startDate = reqJson['date']['start_date']
    endDate = reqJson['date']['end_date']
    
    now = datetime.now()
    current_date = now.strftime("%d-%m-%Y")
    fromAddress = settings.EMAIL_FROM_ADDRESS
    title = 'Ilość wniosków na dzień '+ current_date
    html_message = '<h1>'+ title +':</h1><h2>Od dni: '+ startDate +' do '+ endDate +'</h2><h2>Liczba wniosków:'+ count +'</h2>'
    userList = settings.COUNT_CUSTOM_REQUEST_MAIL_LIST
        
    sendStatus = sendEmail(title, fromAddress, userList, html_message)
    if sendStatus:
        logger.info('WYSLANO EMAIL: Liczba['+ str(sendStatus) +'], OD: '+ fromAddress +', DO: '+ ', '.join(userList) +',Tresc: '+ html_message)
    else:
        logger.error('NIE WYSLANO EMAIL: OD: '+ fromAddress +', DO: '+ ', '.join(userList) +',Tresc: '+ html_message)
    return reqJson