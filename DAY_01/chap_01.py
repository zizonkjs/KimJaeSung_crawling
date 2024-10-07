# 웹페이지 가져오기
# 가장 기본적으로 해야하는 것
from urllib.request import urlopen

html = urlopen('https://www.daangn.com/hot_articles')
print(type(html))
print(html.read())

# beautifulsoup 는 데이타가 있으면 내가 필요한 테그들을 찾아줌.



