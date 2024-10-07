# 트리 이동 : 부모 다루기
from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

#parent 사용
style_tag= soup.style
print(style_tag.parent)

# 부모다루기 2
img1 = soup.find('img', {'src': '../img/gifts/img1.jpg'})
text = img1.parent.previous_sibling.get_text()
print(text)

#parent : 부모 tag를 먼저 검색
# previous_sibling : 부모 태그의 이전 형제 태그 검색
# get_text() : 태그 내부의 문자열 반환
