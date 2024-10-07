# 인터넷 크롤링
# 웹 크롤러를 만들기 전에 고려할 사항
# 수집하려는 데이터는 무엇인가?
# 특정 웹사이트에 도달하면, 새 웹사이트 링크를 따라가야 할까?
# 특정 사이트를 제외 할 것인가?
# 다른 언어를 사용하는 웹사이트 정보 수집 여부
# 저작궘 침해 관련 문제는 없을까?

# 시작 URL : http://oreilly.com

# 정규식
# href=re.compile('^(/|.*' + includeUrl + ')’)
# '/'로 시작하는 링크를 찾음
# ^: 문자열 시작
# ( ) : 그룹
# /|.*: '/' 문자 또는 (|) 임의의 한 문자(.)가 없거나 여러 개 존재 (*: zero or more)

#href = re.compile('^(http|ww)(?!' + excludeUrl +).)*$')
# www로 시작하는 문자열
# excludeUrl 문자열이 존재하지 않는 링크
# 전방 부정 탐색

# 인터넷 크롤링 : URL 구조

from urllib.parse import urlparse

urlString1 = 'https://shopping.naver.com/home/p/index.naver'

url = urlparse(urlString1)
print(url.scheme) # http or https
print(url.netloc) # 인터넷 주소
print(url.path) # 