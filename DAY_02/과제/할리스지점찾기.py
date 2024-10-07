from tabulate import tabulate
from urllib.request import urlopen
import requests
from urllib.parse import quote # 한국어 검색키워드 지원
from bs4 import BeautifulSoup
import csv
import pandas as pd

# 나머지 매장 정보 확인
# 1. 매장 찾기에서 1~50페이지까지 모든 매장의 정보를 스크레이핑
# 지역, 매장명, 매장 주소, 전화번호
# 수집된 정보는 csv 파일로 저장함
# 결과물
# csv파일 : hollys_branches.csv(utf-8로 코딩)

# 기본 URL 설정
base_url = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={}'

# CSV 파일 열기
with open('hollys_store_info.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 헤더 작성
    writer.writerow(['지역', '매장명', '주소', '전화번호'])
    
    # 여러 페이지에 대한 크롤링
    for page_no in range(1, 51):  # 페이지 번호 1~50
        url = base_url.format(page_no)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 테이블 선택 및 데이터 추출
        table = soup.find('table', class_='tb_store')
        rows = table.find_all('tr')[1:]  # 첫 번째 행(헤더 행) 제외


        # 추출한 text 데이터를 csv 파일에 입력하는 반복문
        for row in rows:
            cols = row.find_all('td')
            region = cols[0].text.strip()
            store_name = cols[1].text.strip()
            address = cols[3].text.strip()
            phone = cols[5].text.strip()
            
            # 추출된 데이터를 CSV 파일에 작성
            writer.writerow([region, store_name, address, phone])

print("데이터 크롤링 및 CSV 파일 저장이 완료되었습니다.")





