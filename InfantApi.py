import requests



class InfantWebAPI:
    def __init__(self,domain_url):
        self._domain_url = domain_url
        self._serverstate_url = self._domain_url + 'serverstate.php'
        self._recognize_url = self._domain_url + 'save.php'
        self._informationIOS_url = self._domain_url + 'information_IOS.php'
        self._babyinformation_url = self._domain_url + 'babyinformation.php'
        self._existenceUser_url = self._domain_url + 'identify.php'
        self._correction_url = self._domain_url + "correction.php"
        self._datecheck_url = self._domain_url + "datecheck"
        self._resetmodel_url = self._domain_url + "resetmodel.php"

    def recognize(self,user_account,filepath):
        files = {'file': open(filepath, 'rb')}
        values = {'dirname': user_account}
        datas = {'dirname': user_account,'file': open(filepath, 'rb'),}
        res = requests.post(self._recognize_url, files=files, data=values)	
        return res,self._recognize_url

    def informationIOS(self,user_account,sex='male',date='2018-01-13',country='TW'):
        values = {'country':country,"dirname":user_account,'sex':sex,'date':date,"id":user_account} 
        res = requests.post(self._informationIOS_url,data=values)
        return res,self._informationIOS_url

    def babyinformation(self,user_account,sex='male',date='2018-01-13',country='TW'):
        values = {'country':country,"dirname":user_account,'sex':sex,'date':date,"id":user_account} 
        res = requests.post(self._babyinformation_url,data=values)
        return res,self._babyinformation_url

    def datecheck(self,username):
        values = {'dirname': user_account}
        res = requests.post(self._datecheck_url,data=values)
        return res,self._datecheck_url
    
    def existenceUser(self,user_account,serial):
        values = {"dirname":user_account,"serial":serial} 
        res = requests.post(self._existenceUser_url,data=values)
        return res,self._existenceUser_url

    def correction(self,user_account,data,label_correct,label_correction):
        values = {"dirname":user_account,
            "data":data,
            "correct":label_correct,
            "correction":label_correction} 
        res = requests.post(self._correction_url,data=values)
        return res,self._correction_url

    def resetmodel(user_account):
        values = {'id':user_account}
        res = requests.post(self._resetmodel_url,data=values)
        return res
        

def main():
    domain_url = "https://unicharm.emorec.com.tw/"
    webapi = InfantWebAPI(domain_url)
    account = "bao80275@gmail.com"

    res,url = webapi.informationIOS(user_account = account)    
    print("URL %s\ninformation ios :: [%d] -> %s\n")%(url,res.status_code,res.text)

    res,url = webapi.recognize(user_account=account,filepath='sample/cry0.wav')
    print("URL %s\nrecognize :: [%d] -> %s\n")%(url,res.status_code,res.text)

if __name__ == '__main__':
    main()