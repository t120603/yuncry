#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 09:56:00 2019

@author: jiakwan2
"""

import requests

class InfantCryAPI:
    def __init__(self, url_domain):
        self._url_domain = url_domain
        self._php_serverstate = self._url_domain + 'serverstate.php'
        self._php_recognize = self._url_domain + 'save.php'
        self._php_iOSinfo = self._url_domain + 'information_IOS.php'
        self._php_babyinfo = self._url_domain + 'babyinformation.php'
        self._php_checkuser = self._url_domain + 'identify.php'
        self._php_usercorrection = self._url_domain + 'correction.php'
        self._php_checkdate = self._url_domain + 'datacheck.php'
        self._php_resetmodel = self._url_domain + 'resetmodel.php'
        
    def doRecognize(self, user_account, filepath):
        cryfile = {'file': open(filepath, 'rb')}
        values = {'dirname': user_account}
        #dates = {'dirname': user_account, 'file': open(filepath, 'rb')}
        rtn = requests.post(self._php_recognize, files=cryfile, data=values)
        return rtn, self._php_recognize
    
    def doIOSinfo(self, user_account, sex, date, country='TW'):
        values = {'country': country, 'dirname': user_account, 'sex': sex, 'date': date, 'id': user_account}
        rtn = requests.post(self._php_iOSinfo, data=values)
        return rtn, self._php_iOSinfo
    
    def doBabyinfo(self, user_account, sex, date, country='TW'):
        values = {'country': country, 'dirname': user_account, 'sex': sex, 'date': date, 'id': user_account}
        rtn = requests.post(self._php_babyinfo, data=values)
        return rtn, self._php_babyinfo
    
    def doCheckdate(self, user_account):
        values = {'dirname': user_account}
        rtn = requests.post(self._php_checkdate, data=values)
        return rtn, self._php_checkdate
    
    def doCheckuser(self, user_account, serial_number):
        values = {'dirname': user_account, 'serial': serial_number}
        rtn = requests.post(self._php_checkuser, data=values)
        return rtn, self._php_checkuser
    
    def doFeedback(self, user_account, data, label_correct, label_correction):
        values = {'dirname': user_account,
                  'data': data,
                  'correct': label_correct,
                  'correction': label_correction}
        rtn = requests.post(self._php_usercorrection, data=values)
        return rtn, self._php_usercorrection
    
    def doResetmodel(self, user_account):
        values = {'id': user_account}
        rtn = requests.post(self._php_resetmodel, data=values)
        return rtn, self._php_resetmodel
    