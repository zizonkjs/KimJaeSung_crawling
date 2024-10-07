# 트리 이동

# 문서 내부에서 특정 위치를 기준으로 태그를 찾을 때
# 단방향으로 트리 이동

#트리 이동: 자식과 자손
from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

table_tag = soup.find('table', {'id': 'giftList'})
print('children 개수 : ', len(list(table_tag.children)))

index=0
for child in table_tag.children:
    index +=1
    print(f'[{index}]: {child}')
    print('-'* 30)