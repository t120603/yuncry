# encoding: utf-8
#-*-coding:utf-8 -*-
from InfantApi import *
import sys
from os import listdir, walk
from os.path import isfile, isdir, join
import os
import time
import re
import datetime
import json

def main(domain_url, filePath, filename, fullFilePath, logFileName):
    webapi = InfantWebAPI(domain_url)
    account = 'compal@test.com.tw'
    # fileDirName = re.search(r'[\\\/]*[^\n\\\/]*[a-zA-Z0-9._-]*[\/\\]?$', filePath).group()[1:]
    fileProcess = open(logFileName, "a")
    fileProcess.writelines(filePath + '/' + filename)
    fileProcess.writelines(',')

    res,url = webapi.informationIOS(user_account=account)
    res,url = webapi.addmember(email=account)
    res,url = webapi.babyinformation(user_account = account)
    res, url = webapi.datecheck(user_account=account)
    res,url = webapi.recognize(user_account = account, filepath = fullFilePath)

    try:
        json_response = res.text
        response = json.loads(json_response)
        print('檔案ID:' + str(response['FID']))
        print('標籤:' + str(response['label']) + '\n')
    except:
        print('Exception !! \n')
        print(res)

    if re.match('<html>', res.text):
        if res.status_code == 413:
            print('Too Large!!')
        elif res.status_code == 504:
            print('Time Out!!')
        fileProcess.writelines('Http_' + str(res.status_code))
    elif res.text == '':
        fileProcess.writelines('Http_' + str(res.status_code))
    else:
        fileProcess.writelines(res.text)

    fileProcess.writelines('\n')
    fileProcess.close()


if __name__ == '__main__':
    url = 'http://140.125.179.121:8888/' # Request Address

    path=sys.argv[1] # Audio File Path
    files=listdir(path)

    # 建立log輸出位置
    outputLogPath = "./log/"
    print("outputLogPath: " + outputLogPath)

    if not os.path.exists(outputLogPath):
        os.makedirs(outputLogPath)

    outputDirName = re.search(r'[\\\/]*[^\n\\\/]*[a-zA-Z0-9._-]*[\/\\]?$', path).group()[1:-1]
    print('outputDirName: ' + outputDirName)
    logFileName = outputLogPath + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S_")) + outputDirName + '.csv'
    print('Log File: ' + logFileName)

    for dirPath, dirNames, fileNames in walk(path):
        for f in (fileNames):
            fullFilePath = join(dirPath, f) #result: dir/file
            if isfile(fullFilePath):
                print(fullFilePath)
                main(url, dirPath, f, fullFilePath, logFileName)
