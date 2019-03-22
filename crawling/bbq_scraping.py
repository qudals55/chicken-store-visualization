import time
from selenium import webdriver
from itertools import count
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def crawling_goobne():

    url = 'http://changup.bbq.co.kr/findstore/findstore_list.asp'




    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")
    options.add_argument("lang=ko_KR") # 한국어!

    wd = webdriver.Chrome('./chromedriver', chrome_options=options)

    wd.get(url)
    wd.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5]}})")
    wd.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")



    results = []

    for page in range(1,138):

        script = 'schPaging(%d)' % page

        wd.execute_script(script)
        time.sleep(1)
        html = wd.page_source
        bs = BeautifulSoup(html, 'html.parser')
        tag_body = bs.select_one("#datazone > table > tbody")
        tags_tr = tag_body.findAll('tr')
        # print(tags_tr)
        cnt = 0
        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[3]
            str_ = str(address).split(' ')
            if len(str_) != 1:
                results.append((name, address, str_[0], str_[1]))



    table = pd.DataFrame(results, columns=['name', 'address', 'city', 'rigeon'])

    table.to_csv('bbq.csv')



if __name__ == '__main__':

    print('비비큐 매장 크롤링 시작')
    crawling_goobne()
    print('비비큐 매장 크롤링 종료')
