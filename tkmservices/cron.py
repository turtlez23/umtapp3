from datetime import datetime

from django.conf import settings

from .views import checkOnlineCustomerRequest, sendEmail

def sendMailWithOnlineCustomRequests():
    reqJson = checkOnlineCustomerRequest()
    objs = reqJson['response']
    count = str(len(objs))    
    now = datetime.now()
    current_date = now.strftime("%d-%m-%Y")
    title = 'Ilość wniosków online na dzień '+ current_date
    html_message = '<h1>'+ title +':</h1><h2>'+ count +'</h2>'
    if not count:
        html_message += '<h2>BRAK WNIOSKÓW ONLINE NA DZIEŃ: '+ current_date +'</h2>'
    else:
        for obj in objs:
            html_message += '<p>'+ obj['id'] +'</p>'
    
    sendEmail(title, settings.EMAIL_FROM_ADDRESS, settings.ONLINE_CUSTOM_REQUEST_MAIL_LIST, html_message)

    return html_message