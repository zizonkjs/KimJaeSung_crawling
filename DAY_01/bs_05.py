html_example	='''
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BeautifulSoup 활용</title>
</head>
<body>
    <h1 id="heading">Heading 1</h1>
    <p>Paragraph</p>
    <span class="red">BeautifulSoup Library Examples!</span>
    <div id="link">
        <a class="external_link" href="www.google.com">google</a>

        <div id="class1">
            <p id="first">class1's first paragraph</p>
            <a class="exteranl_link" href="www.naver.com">naver</a>

            <p id="second">class1's second paragraph</p>
            <a class="internal_link" href="/pages/page1.html">Page1</a>
            <p id="third">class1's third paragraph</p>
        </div>
    </div>
    <div id="text_id2">
        Example page
        <p>g</p>
    </div>
    <h1 id="footer">Footer</h1>
</body>
</html>
'''

#select_one()
# 첫 번째 일치하는 태그만 리턴 : find()와 동일 기능
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_example, 'html.parser')
head = soup.select_one('head')
print(head)
print('head.text:', head.text.strip())

h1 = soup.select_one('h1')
print (h1)

# select_one() 함수 예제
footer = soup.select_one('h1#footer')
print(footer)

# 클래스 이름 검색 : 태그.클래스이름
class_link = soup.select_one('a.internal_link')
print(class_link)

print(class_link.string)
print(class_link['href'])

# 부모 > 자시 태그 형식으로 접근
link1 = soup.select_one('div#link > a.external_link')
print(link1)

# find 함수와 비교
link_find = soup.find('div', {'id':'link'})

external_link = link_find.find('a', {'class':'external_link'})
print('find external_link: ', external_link)

# 계층적 하위 접근
link2 = soup.select_one('div#class1 p#second')
print(link2)
print(link2.string)

internal_link = soup.select_one('div#link a.internal_link')
print(internal_link['href'])
print(internal_link.text)

# select() == find_all()
div_urls = soup.select('div#class1 > a')

print(div_urls)
print(div_urls[0]['href'])

#여러 항목 검색하기
h1 = soup.select('#heading, #footer')
print(h1)

url_links = soup.elect('a.external_link, a.internal_link')
print(url_links)

