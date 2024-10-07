# 시가 총액 10위 까지의 기업 정보를 크롤링
# 네이버 금융 웹사이트

# 크롤링 항목 7개 출력
# 종목명, 종목코드, 현재가, 전일가, 시가, 고가, 저가
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parse
import pandas as pd
import collections
from tabulate import tabulate
import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


if not hasattr(collections, 'Callable'):
    collections.Callable = collections.abc.Callable


# 웹드라이버 설정
driver = webdriver.Chrome()

# CSV 파일 생성 및 헤더 작성
with open('stock_info.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['종목명', '종목코드', '현재가', '전일가', '시가', '고가', '저가'])

    # 네이버 금융 시가총액 페이지로 이동
    driver.get('https://finance.naver.com/sise/sise_market_sum.naver')

    # 1부터 10까지 차례대로 클릭하여 데이터 수집
    for i in range(1, 11):
        # 각 종목의 링크 클릭
        item_xpath = f'//td[@class="no"][text()="{i}"]/following-sibling::td/a'
        stock_link = driver.find_element(By.XPATH, item_xpath)
        stock_name = stock_link.text  # 종목명
        stock_link.click()

        # 페이지 로드 대기
        time.sleep(2)

        # HTML 파싱
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        try:
            # 종목명 추출
            stock_name_tag = soup.find('h2')
            stock_name = stock_name_tag.text.strip() if stock_name_tag else "N/A"

            # 종목코드 추출
            stock_code_tag = soup.find('span', {'class': 'code'})
            stock_code = stock_code_tag.text.strip() if stock_code_tag else "N/A"

            

            # <dl> 태그에서 필요한 값 추출
            data_list = soup.find('dl', {'class': 'blind'}).find_all('dd')

            now_price = data_list[3].text.split()[1]  # 전일가
            previous_close = data_list[4].text.split()[-1]  # 전일가
            opening_price = data_list[5].text.split()[-1]   # 시가
            high_price = data_list[6].text.split()[-1]      # 고가
            low_price = data_list[8].text.split()[-1]       # 저가

            '''<dl class="blind">
	        <dt>종목 시세 정보</dt>
	        <dd>2024년 08월 13일 16시 11분 기준 장마감</dd>
	        <dd>종목명 삼성전자</dd>
	        <dd>종목코드 005930 코스피</dd>
	        <dd>현재가 76,100 전일대비 상승 600 플러스 0.79 퍼센트</dd>
	        <dd>전일가 75,500</dd>
	        <dd>시가 76,500</dd>
	        <dd>고가 76,600</dd>
	        <dd>상한가 98,100</dd>
	        <dd>저가 75,500</dd>
	        <dd>하한가 52,900</dd>
	        <dd>거래량 10,599,575</dd>
	        <dd>거래대금 805,996백만</dd>
        </dl> 이 요소들은 각각 str문자열이기 때문에 slice가능하다!'''

            # CSV 파일에 데이터 저장
            writer.writerow([stock_name, stock_code, now_price, previous_close, opening_price, high_price, low_price])
        
        except Exception as e:
            print(f"Error while parsing data for {stock_name} ({stock_code}): {e}")

        # 다시 시가총액 페이지로 이동
        driver.back()
        time.sleep(2)

# 브라우저 종료
driver.quit()


