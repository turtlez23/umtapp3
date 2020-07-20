# -*- coding: utf-8 -*- 
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from datetime import datetime, timedelta
from django.test import TestCase
from django.conf import settings
from .views import sendEmail, checkOnlineCustomerRequest, tkmCountDuplicateAndRegistrationCustomerRequest
from .cron import sendMailWithOnlineCustomRequests, sendmailWithCountBillingWeekDuplicateAndRegistrationCustomerRequest

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
    def test_checkOnlineCustomerRequest(self):
        print('\n### START ### test_checkOnlineCustomerRequest ####################\n')
        print(checkOnlineCustomerRequest())
        print('\n### END ### test_checkOnlineCustomerRequest ####################\n')

    def test_sendMailWithOnlineCustomRequests(self):
        print('\n### START ### test_sendMailWithOnlineCustomRequests ####################\n')
        print(sendMailWithOnlineCustomRequests())
        print('\n### END ### test_sendMailWithOnlineCustomRequests ####################\n')

    def test_tkmCountDuplicateAndRegistrationCustomerRequest(self):
        print('\n### START ### test_tkmCountDuplicateAndRegistrationCustomerRequest ####################\n')
        datetime.time 
        startDate = datetime.now() - timedelta(days=7)
        endDate = datetime.now() - timedelta(days=1)
        startDateStr = startDate.strftime(settings.DATE_FORMAT)
        endDateStr = endDate.strftime(settings.DATE_FORMAT)
        print(tkmCountDuplicateAndRegistrationCustomerRequest(startDateStr, endDateStr))
        print('\n### END ### test_tkmCountDuplicateAndRegistrationCustomerRequest ####################\n')

    def test_sendmailWithCountBillingWeekDuplicateAndRegistrationCustomerRequest(self):
        print('\n### START ### test_sendmailWithCountBillingWeekDuplicateAndRegistrationCustomerRequest ####################\n')
        json = sendmailWithCountBillingWeekDuplicateAndRegistrationCustomerRequest()
        print(json)

        start = datetime.strptime(json['date']['start_date'], settings.DATE_FORMAT)
        end = datetime.strptime(json['date']['end_date'], settings.DATE_FORMAT)

        self.assertLessEqual(start, end)
        print('\n### END ### test_sendmailWithCountBillingWeekDuplicateAndRegistrationCustomerRequest ####################\n')