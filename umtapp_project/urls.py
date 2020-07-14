# -*- coding: utf-8 -*- 
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from django.urls import path, include

from tarnow_pl import views as api_tarnow_pl_views

from tkmservices import views_parkometer_api
from tkmservices import views_ticketvalidate_api
from tkmservices import views_printcard_api

#admin.autodiscover()
urlpatterns = [
    path('admin/', admin.site.urls),
	
    path('', include('home.urls')),	
    path('epuap/', include('epuap.urls')),    
	path('tarnow_pl/', include('tarnow_pl.urls')),
	path('tkmservices/', include('tkmservices.urls')),

    # API URLS    
	    # TARNOW_PL
    path('api/v1/getDataFromTarnowPl/', api_tarnow_pl_views.getDataFromTarnowPl, name='getDataFromTarnowPl'),
        # TKMSERVICES
            # API PRK
    # Count all prk
    path('api/v1/tkmservices/parkometer/tkmParkometerTransactionsCountAll/', views_parkometer_api.tkmParkometerTransactionsCountAll, name='parkometer'),
    # Count all prk with devices name
    path('api/v1/tkmservices/parkometer/tkmParkometerTransactionsCountAllDevices/', views_parkometer_api.tkmParkometerTransactionsCountAllDevices, name='parkometer-devices'),
    # get all prk devices
    path('api/v1/tkmservices/parkometer/tkmGetAllParkometerDevices/', views_parkometer_api.tkmGetAllParkometerDevices, name='get-parkometer-devices'),
    # get one prk devices
    path('api/v1/tkmservices/parkometer/tkmParkometerTransactionsOneDevices/', views_parkometer_api.tkmParkometerTransactionsOneDevices, name='get-one-parkometer-tran'),
    # Count one prk devices
    path('api/v1/tkmservices/parkometer/tkmParkometerTransactionsCountOneDevices/', views_parkometer_api.tkmParkometerTransactionsCountOneDevices, name='count-one-parkometer-tran'),
            # API TICKET
    # Count myself fellow ticket validate
    path('api/v1/tkmservices/ticketvalidate/tkmMyselfFellowCount/', views_ticketvalidate_api.tkmMyselfFellowCount, name='myself-fellow-count'),
    path('api/v1/tkmservices/ticketvalidate/tkmMyselfFellowWithVariantCount/', views_ticketvalidate_api.tkmMyselfFellowWithVariantCount, name='myself-fellow-variant-count'),
    path('api/v1/tkmservices/ticketvalidate/tkmLineSocialGroupFromClientTableCount/', views_ticketvalidate_api.tkmLineSocialGroupFromClientTableCount, name='tkmLineSocialGroupFromClientTableCount'),
    path('api/v1/tkmservices/ticketvalidate/tkmLineSocialGroupFromTpTableCount/', views_ticketvalidate_api.tkmLineSocialGroupFromTpTableCount, name='tkmLineSocialGroupFromTpTableCount'),
    path('api/v1/tkmservices/ticketvalidate/tkmTicketValidateHistory/', views_ticketvalidate_api.tkmTicketValidateHistory, name='tkmTicketValidateHistory'),
            # API PRINT CARD
	path('api/v1/tkmservices/printcard/tkmPdfExport/', views_printcard_api.tkmPdfExport, name='tkmPdfExport'),
	path('api/v1/tkmservices/printcard/tkmPdfMultipleExport/', views_printcard_api.tkmPdfMultipleExport, name='tkmPdfMultipleExport'),
    # No use
	# path('api/v1/tkmservices/printcard/tkmGetPhotoList/', views_printcard_api.tkmPdfExport, name='tkmGetPhotoList'),
    

]
