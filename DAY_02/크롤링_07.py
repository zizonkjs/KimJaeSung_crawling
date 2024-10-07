# 네이버 블로그 검색
from urllib.request import urlopen
import requests
from urllib.parse import quote # 한국어 검색키워드 지원
from bs4 import BeautifulSoup

query='chatGPT' # 검색어
url =	f'https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=chatGPT'

html = urlopen(url)
soup = BeautifulSoup(html.read(), 'html.parser')
blog_results = soup.select('a.title_link')
print('검색 결과수:', len(blog_results))
search_count = len(blog_results)
desc_results = soup.select('a.dsc_link')

for i in range(search_count):
    title = blog_results[i].text
    link = blog_results[i]['href']
    print(f'{title}, [{link}]')
    print(desc_results[i].text)
    print('-'*80)

