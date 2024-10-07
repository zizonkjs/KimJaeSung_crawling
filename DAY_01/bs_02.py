# find() 함수

from urllib.request import urlopen
from bs4 import BeautifulSoup
html_example	=	'''
 <!DOCTYPE	html>
 <html	lang="en">
 <head>
 <meta	charset="UTF-8">
 <meta	name="viewport"	content="width=device-width,	initial-scale=1.0">
 <title>BeautifulSoup	활용</title>
 </head>
 <body>
 <h1	id="heading">Heading	1</h1>
 <p>Paragraph</p>
 <span	class="red">BeautifulSoup	Library	Examples!</span>
 <div	id="link">
 <a	class="external_link"	href="www.google.com">google</a>
 <div	id="class1">
 <p	id="first">class1's	first	paragraph</p>
 <a	class="external_link"	href="www.naver.com">naver</a>
 <p	id="second">class1's	second	paragraph</p>
 <a	class="internal_link"	href="/pages/page1.html">Page1</a>
 <p	id="third">class1's	third	paragraph</p>
 </div>
 </div>
 <div	id="text_id2">
 Example	page
 <p>g</p>
 </div>
 <h1	id="footer">Footer</h1>
 </body>
 </html>
 '''
soup = BeautifulSoup(html_example, 'html.parser')
# 여러 <div> 태그 중 특정 속성을 가지는 항목 추출 -> 많이 씀
# - 딕셔너리 형태로 입력 ( id속성의 값이 'text_id2'인 항목 검색)
print(soup.find('div',{'id':'text_id2'}))

div_text = soup.find('div', {'id': 'text_id2'})
print(div_text.text)

print(div_text.string)

#find() 함수 활용'
# <a> 태그 중 class 속성값이 'internal_link'인 정보 추출
href_link = soup.find('a', {'class': 'internal_link'})
href_link = soup.find('a', class_='internal_link')

print(href_link)
print(href_link['href'])
print(href_link.get('href'))
print(href_link.text)

# <a> 태그 내부의 모든 속성 가져오기 : attrs
print('href_link.attrs: ', href_link.attrs)
# print('class 속성값: ', href_link['Class'])

print('values():', href_link.attrs.values())

# values = list(href_link.attrs.values())
# print(f'values[0]: {values[0]}, values[1]:{values[1]}')

# href 속성의 값이 www.gogle.com인 항목검색
#속성 : attrs={'속성이름' : '속성값'}

href_value = soup.find(attrs={'href':'www.google.com'})
href_value = soup.find('a', attrs={'href':'www.google.com'})

print('href_vlaue:', href_value)
print(href_value['href'])
print(href_value.string)

# find() 함수
# span 태그의 속성 가져오기
span_tag = soup.find('span')
print('span tag:', span_tag)
print('attrs:', span_tag.attrs)
print('value:', span_tag.attrs['class'])
print('text:', span_tag.text)

# class 속성
# class 속성은 여러 개의 값을 가질 수 있음
# 따라서 list 형태로 리턴함
print('class 속성값:', href_link['class'])


