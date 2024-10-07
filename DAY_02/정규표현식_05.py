# 정규 표현식과 BeautifulSoup

# BeautifulSoup의 문자열을 받는 함수들
# 정규 표현식을 매개 변수로 받을 수 있음

# 제품 이미지 검색

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

img_tag = re.compile('/img/gifts/img.*.jpg') # -> *(임의의 문자)
images = soup.find_all('img', {'src':img_tag})

for image in images:
    print(image, end="	->	['src']	속성값:	")
    print(image['src']) # 이미지 속성의 대한 값
    