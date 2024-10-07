# 링크간 무작위 이동하기 : 동작 과정
# gotLinks(articleUrl) 함수 작성
# 파라미터 : 임의의 '/wiki/<article_name>' 형태를 받음
# 리턴값 : 해당 링크의 모든 URL 목록을 리턴(리스트 형태)

# 동작 과정
# 시작 URL : 입력
# 시작 URL 내부의 연관 기사 URL을 가져옴
# 연관 기사 URL에서 랜덤하게 하나의 URL선택
# 선택된 URL로 이동해서 다시 연관 기사 URL을 가져오는 과정 반복
# 무한 반복

from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import re

random.seed(None) # 난수 발생기 초기화, None : 현재시스템 시간을 사용

def getLinks(articleUrl):
    html = urlopen('https://en.wikipedia.org'+ articleUrl)
    bs = BeautifulSoup(html, 'html.parser')
    bodyContent = bs.find('div', {'id': 'bodyContent'})
    wikiUrl = bodyContent.find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
    return wikiUrl

links = getLinks('/wiki/Kevin_Bacon')
print('links 길이:', len(links))
while len(links) > 0 :
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)

