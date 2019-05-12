#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 09:56:00 2019

@author: jiakwan2
"""

from infantcry import *
import sys
import time

whichServer = input("Which server you choose? (1: testcry, 2: unicharm)) > ")
if whichServer == '1':
    goURL = InfantCryAPI("https://testcry.emorec.com.tw")
    gender = 'male'
    tester = "A6CDLDXPNNURBG9YSPHJ@kramxel.com"
elif whichServer == '2':
    goURL = InfantCryAPI("https://unicharm.emorec.com.tw/")
    gender = 'female'
    tester = "t120603@gmail.com"
else:
    sys.exit()

fname = input("Enter the crying filename: ")
cryfile = 'sample/'+fname
today = time.strftime("%Y-%m-%d", time.localtime())
    
res, doapi = goURL.doIOSinfo(user_account=tester,sex=gender, date=today)
if res.status_code != 200:
    print("ERR @ InfantWebAPI:informationIOS, status_code is %d\n"%(res.status_code))
    sys.exit()
res, doapi = goURL.doRecognize(tester, filepath=cryfile)

if res.status_code != 200:
    print("ERR @ InfantWebAPI:recognize, status_code is %d\n"%(res.status_code))
    sys.exit()
print("==> CRY recognition for %s is <%s>\n"%(fname, res.text))
    
# feedback
feedback = input("\tDo you want to correct the recognition result? ")
if feedback == 'yes' or feedback == 'YES' or feedback == 'y' or feedback == 'Y':
    user_correct = ("\tWhat's the reason of baby crying? (Pain / Sleepy / Diaper / Hungry / Other)")
    res, doapi = goURL.doFeedback(tester, data=today, local_correct='Yes', label_correction=user_correct)
    if res.status_code != 200:
        print("ERR @ InfantWebAPI:correction, status_code is %d\n"%(res.status_code))

