import sys
import csv
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

def address(state, city) :
    return ({ '경기' : '경기도',
            '서울' : '서울특별시',
            '서울시' : '서울특별시',
            '인천' : '인천광역시',
            '인천시' : '인천광역시',
            '제주' : '제주특별자치도',
            '전남' : '전라남도',
            '전북' : '전라북도',
            '경북' : '경상북도',
            '경남' : '경상남도',
            '부산' : '부산광역시',
            '울산' : '울산광역시',
            '대구' : '대구광역시',
            '충북' : '충청북도',
            '충남' : '충청남도',
            '세종시' : '세종특별자치시',
            '세종' : '세종특별자치시',
            '대전' : '대전광역시',
            '강원' : '강원도',
            '광주' : '광주광역시',
            }.get(state, state), city)
        
def main():
    driver = webdriver.PhantomJS()
    idx = 1
    f = open('cheogajip.csv', 'w', encoding='utf-8', newline='')
    wr = csv.writer(f, delimiter=',')
    wr.writerow(['매장이름', '시도정보', '시군구정보', '매장주소'])
    while idx <= 105:
        driver.get("http://www.cheogajip.co.kr/bbs/board.php?bo_table=store&page=" + str(idx))
        
        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')
        chickens = soup.select('#fboardlist > div > table > tbody > tr')
        
        for chicken in chickens :
            shopName = chicken.select('td[class=td_date]')[1].text
            shopAdd = chicken.select_one('td[class=td_subject]').text
            shopAdd = re.sub('\n', '', shopAdd)
            shopAddSplit = shopAdd.split()
            state, city = address(shopAddSplit[0], shopAddSplit[1])
            wr.writerow([shopName, state, city, shopAdd])
        idx = idx + 1
    f.close()

    print('end')
if __name__ == '__main__':
    main()