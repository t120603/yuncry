from InfantApi import *
import sys

def main(domain_url):
	webapi = InfantWebAPI(domain_url) 
	account = "A6CDLDXPNNURBG9YSPHJ@kramxel.com"

	res,url = webapi.informationIOS(user_account = account)    
	print("URL %s\ninformation ios :: [%d] -> %s\n")%(url,res.status_code,res.text)

	res,url = webapi.babyinformation(user_account = account)    
	print("URL %s\nbabyinformation :: [%d] -> %s\n")%(url,res.status_code,res.text)

	res,url = webapi.existenceUser(user_account = account,serial='123')    
	print("URL %s\nexistenceUser :: [%d] -> %s\n")%(url,res.status_code,res.text)

	res,url = webapi.recognize(user_account=account,filepath='sample/cry0.wav')
	print("URL %s\nrecognize :: [%d] -> %s\n")%(url,res.status_code,res.text)

	res,url = webapi.correction(user_account=account,data='2017-06-13',label_correct='No',label_correction='Sleepy')
	print("URL %s\ncorrection :: [%d] -> %s\n")%(url,res.status_code,res.text)

if __name__ == '__main__':
    url = sys.argv[1]
    main(url)
