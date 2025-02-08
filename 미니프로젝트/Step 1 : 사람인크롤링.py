'''
이 코드는 Selenium과 BeautifulSoup을 이용하여 사람인(saramin.co.kr)에서 "AI 관련 채용 공고" 데이터를 수집하고, CSV 파일로 저장하는 자동화 스크립트입니다.

📌 주요 동작 과정
웹드라이버 실행

webdriver.Chrome()을 실행하여 크롬 브라우저를 엽니다.
사람인 AI 채용 공고 페이지 이동

driver.get(url)을 통해 해당 URL의 페이지로 이동한 후, time.sleep(5)로 페이지가 완전히 로딩될 때까지 기다립니다.
HTML 페이지 소스 가져오기 및 파싱

driver.page_source로 페이지 HTML을 가져온 후, BeautifulSoup을 사용하여 HTML을 파싱합니다.
CSV 파일 생성 및 헤더 작성

'saramin_jobs.csv3' 파일을 생성하고, **헤더(회사이름, 채용정보, 채용조건, Job Sector)**를 추가합니다.
채용 공고 데이터 크롤링

soup.find('div', class_='list_body')에서 공고 리스트를 찾고,
각 div.box_item 요소에서
회사 이름 (company_nm)
채용 정보 (job_tit)
채용 조건 (recruit_info)
직무 분야 (job_sector)
를 추출합니다.
CSV 파일 저장

추출한 데이터를 CSV 파일에 한 줄씩 저장합니다.
브라우저 종료

driver.quit()을 호출하여 크롤링이 끝나면 크롬 브라우저를 닫습니다.
'''
from selenium import webdriver
from bs4 import BeautifulSoup
import collections
import time

if not hasattr(collections, 'Callable'):
    collections.Callable = collections.abc.Callable
import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# 웹드라이버 설정
driver = webdriver.Chrome()

# 사라민 페이지로 이동
url = 'https://www.saramin.co.kr/zf_user/jobs/list/job-category?page=1&cat_mcls=2&loc_mcd=104000&searchword=AI&searchType=recently&search_optional_item=y&search_done=y&panel_count=y&preview=y&isAjaxRequest=0&page_count=100&sort=RL&type=job-category&is_param=1&isSearchResultEmpty=1&isSectionHome=0&searchParamCount=3&tab=job-category'
driver.get(url)
time.sleep(5)  # 페이지 로딩 대기

# 페이지 소스 가져오기
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# CSV 파일 생성 및 헤더 작성
with open('saramin_jobs.csv3', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['회사이름', '채용정보', '채용조건', 'Job Sector'])

    # 각 채용공고 크롤링
    job_items = soup.find('div', class_='list_body').find_all('div', class_='box_item')

    for item in job_items:
        company_name = item.find('div', class_='company_nm').get_text(strip=True)
        job_info = item.find('div', class_='job_tit').get_text(strip=True)
        job_condition = item.find('div', class_='recruit_info').get_text(strip=True)
        
        job_sector_tags = item.find('span', class_='job_sector').find_all('span')
        job_sector = ', '.join([tag.get_text(strip=True) for tag in job_sector_tags])

        writer.writerow([company_name, job_info, job_condition, job_sector])

# 브라우저 종료
driver.quit()
