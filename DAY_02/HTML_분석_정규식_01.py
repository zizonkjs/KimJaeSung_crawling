# 복잡한 웹페이지에서 필요한 정보 가져오기
# 원하지 않는 콘텐츠 제거하기


#find 함수에 이름, 속성, 속성값을 이용하여 원하는 태그를 검색
from bs4 import BeautifulSoup

html_text='<span	class="red">Heavens!	what	a	virulent	attack!</span>'
# Class -> 속성
# "red" -> 속성값 
# 리스트 형태로 반환
soup = BeautifulSoup(html_text, 'html.parser')

object_tag = soup.find('span')
print('object_tag:', object_tag)
print('attrs:', object_tag.attrs)
print('value:', object_tag.attrs['class'])
print('text:', object_tag.text)



