# -*- coding: utf-8 -*- 
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from .views import sendEmail, checkOnlineCustomerRequest
from.cron import sendMailWithOnlineCustomRequests

# class EmailTest(TestCase):
#     def test_send_email(self):
#         print('test_send_email')
#         countSendingValue = sendEmail(title, fromAddress, toAddress, html_message)
#         self.assertEqual(countSendingValue, 1)
#         print(str(countSendingValue) +' ?= 1')
    # def test_checkOnlineUserRequest(self):
    #     reqJson = checkOnlineCustomerRequest()
    #     self.assertEqual(reqJson['status'], '200')
    #     print(str(reqJson))

class CronMethodTest(TestCase):
    def test_sendMailWithOnlineCustomRequests(self):
        print(sendMailWithOnlineCustomRequests())