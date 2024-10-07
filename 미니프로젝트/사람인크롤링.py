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