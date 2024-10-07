# iframe 접근
# iframe: 현재 페이지에 다른 웹 페이지를 부럴와서 삽입시킬 수 있음

# 크롤링이 안됄 때 iframe이 있는지 확인
# switch_to.frame('mainframe') -> 프레임 건너뛰는 코드

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parse
import pandas as pd
import collections
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://blog.naver.com/swf1004/221631056531')

driver.switch_to.frame('mainFrame')

if not hasattr(collections, 'Callable'):
    collections.Callable = collections.abc.Callable

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

results = soup.find_all('div', {'class': 'se-module'})
for result in results:
    remove_carriage_str = result.text.replace('\n','')
    print(remove_carriage_str)
    result.append(remove_carriage_str)