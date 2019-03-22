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
            return response.read().decode('utf-8')
    except Exception as e:
        return None

def getKyochonAddress():
    for sido1 in range(1,18):
        for sido2 in count():
            url = 'http://www.kyochon.com/shop/domestic.asp'
            url += '?txt_search='
            url += '&sido1=%s' %str(sido1)
            url += '&sido2=%s' %str(sido2 +1)

            mydata = get_request_url(url)
            if(mydata == None):
                break
            soup = BeautifulSoup(mydata, 'html.parser')
            ultag = soup.find('ul', attrs={'class':'list'})

            for myitem in ultag.findAll('a', href=True):
                store = myitem.find('dt').get_text()
                address = myitem.find('dd').get_text()
                address = address.strip().split('\r')[0]

                imsi = address.split(' ')
                sido = imsi[0]
                gungu = imsi[1]

                sublist = []
                sublist.append(store)
                sublist.append(sido)
                sublist.append(gungu)
                sublist.append(address)

                result.append(sublist)

print('kyochon 매장 크롤링 시작')
getKyochonAddress()
data = pd.DataFrame(result, columns = myColumns)
data.to_csv('kyochon.csv', encoding = myencoding, mode = 'w', index=True )
print('kyochon 매장 크롤링 종료')
