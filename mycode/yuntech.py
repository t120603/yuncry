#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 09:56:00 2019

@author: jiakwan2
"""

from infantcry import *
import sys
import time

def main(whichServer, fname):
    if (whichServer == 'testcry'):
        goURL = InfantCryAPI("https://testcry.emorec.com.tw")
        gender = 'male'
        tester = "A6CDLDXPNNURBG9YSPHJ@kramxel.com"
    else:
        goURL = InfantCryAPI("https://unicharm.emorec.com.tw/")
        gender = 'female'
        tester = "t120603@gmail.com"
    today = time.strftime("%Y-%m-%d", time.localtime())
    cryfile = 'sample/'+fname
    
    res, doapi = goURL.doIOSinfo(user_account=tester,sex=gender, date=today)
    if res.status_code != 200:
        print("ERR @ InfantWebAPI:informationIOS, status_code is %d\n"%(res.status_code))
        return
    res, doapi = goURL.doRecognize(tester, filepath=cryfile)
    if res.status_code != 200:
        print("ERR @ InfantWebAPI:recognize, status_code is %d\n"%(res.status_code))
        return
    print("==> CRY recognition for %s is <%s>\n"%(fname, res.text))
    
    # feedback
    feedback = input("\tDo you want to correct the recognition result? ")
    if feedback == 'yes' or feedback == 'YES' or feedback == 'y' or feedback == 'Y':
        user_correct = ("\tWhat's the reason of baby crying? (Pain / Sleepy / Diaper / Hungry / Other)")
        res, doapi = goURL.doFeedback(tester, data=today, local_correct='Yes', label_correction=user_correct)
        if res.status_code != 200:
            print("ERR @ InfantWebAPI:correction, status_code is %d\n"%(res.status_code))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Format error!! Please enter 'python service-name cry-filename'\n")
        sys.exit()
    
    param1 = sys.argv[1]
    param2 = sys.argv[2]
    main(param1, param2)
    