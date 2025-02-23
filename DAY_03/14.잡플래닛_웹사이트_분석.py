import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from tabulate import tabulate

company_dict = {'삼성전자':'https://www.jobplanet.co.kr/companies/30139/reviews/삼성전자',
'LG전자':'https://www.jobplanet.co.kr/companies/19514/reviews/lg전자',
'SK하이닉스':'https://www.jobplanet.co.kr/companies/20561/reviews/에스케이하이닉스',
'네이버':'https://www.jobplanet.co.kr/companies/42217/reviews/네이버'}

xpath_dict = {'전체평점':'//*[@id="premiumReviewStatistics"]/div[2]/div[1]/div/div[1]/div[1]/span[1]',
'복지':	'//*[@id="premiumReviewStatistics"]/div[2]/div[1]/div/div[1]/div[2]/div/div/div[1]/div[2]/span[2]',
'업무와 삶의 균형':'//*[@id="premiumReviewStatistics"]/div[2]/div[1]/div/div[1]/div[2]/div/div/div[2]/div[2]/span[2]',
'사내문화':'//*[@id="premiumReviewStatistics"]/div[2]/div[1]/div/div[1]/div[2]/div/div/div[3]/div[2]/span[2]',
'승진 기회':'//*[@id="premiumReviewStatistics"]/div[2]/div[1]/div/div[1]/div[2]/div/div/div[4]/div[2]/span[2]',
'경영진':'//*[@id="premiumReviewStatistics"]/div[2]/div[1]/div/div[1]/div[2]/div/div/div[5]/div[2]/span[2]'}

driver = webdriver.Chrome()

compary_score_dict = {}
for company_name in company_dict.keys():
    score_list = []
    company_url = company_dict.get(company_name)
    driver.get(company_url)

    #회사이름 가져오기
    company = driver.find_element(By.CLASS_NAME, 'name').text
    print(company)

    for key in xpath_dict.keys():
        # 전체 5개의 평점 가져오기
        point = driver.find_element(By.XPATH, xpath_dict.get(key)).text
        print(f'{key}: {point}', end=' ')
        score_list.append(point)
    print()
    # 딕셔너리에 모든 평점 추가하기
    compary_score_dict[company_name] = score_list

print('company_score_dict')
for key in compary_score_dict.keys():
    print(f'{key}:{compary_score_dict.get(key)}')

# 딕셔너리를 DataFrame 으로 변환
columns=('전체평점', '복지', '업무와 삶의 균형', '사내문화', '승진 기회', '경영진')

# 딕셔너리의 키가 행의 색인이 되고 딕셔너리의 값이 행의 데이터가 됨
company_score_df = pd.DataFrame.from_dict(compary_score_dict, orient='index', columns=columns)

print(tabulate(company_score_df, headers='keys', tablefmt='psql'))

