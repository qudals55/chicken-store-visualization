import pandas as pd
import urllib.request
import datetime
import json
from bs4 import BeautifulSoup
from itertools import count

result = []
myColumns = ('store', 'sido', 'gungu','address')
myencoding = 'utf-8'

def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print ("[%s] Url Request Success" % datetime.datetime.now())
            return response
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def getPRCNaddress():
    for page_idx in count():
        url = "http://www.pelicana.co.kr/store/stroe_search.html?page=%d" %(page_idx+1)
        mydata = get_request_url(url)
        soup = BeautifulSoup(mydata, 'html.parser')

        mytable = soup.find('table',{'class':'table mt20'})

        mytbody = mytable.find('tbody')
        bEnd = True

        for mytr in mytbody.findAll('tr'):
            bEnd = False
            mylist = list(mytr.strings)
            store = mylist[1]
            address = mylist[3]
            imsi = address.split(' ')
            sido = imsi[0]
            gungu = imsi[1]

            sublist = []
            sublist.append(store)
            sublist.append(sido)
            sublist.append(gungu)
            sublist.append(address)
            result.append(sublist)

        if(bEnd == True) :
            return

print('페리카나 매장 크롤링 시작')
getPRCNaddress()
data = pd.DataFrame(result, columns = myColumns)
data.to_csv('PRCN.csv', encoding = myencoding, mode = 'w', index=True )
print('페리카나 매장 크롤링 종료')
