from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser') # -> parsing 클래스의 생성자 -> 객체 생성
print(bs)
# print(bs.h1) # 사이트에서 첫번째 <1h>태그만 반환
# print(bs.h1.string) # bs 의 h1안에 문자열 반환
print(bs.div.text)
print(bs.div) # 태그까지 전부 가져옴

# 내가 원하는 소스의 위치를 파악해야함
# 크롤링 할때는 body 부분을 봐야함
