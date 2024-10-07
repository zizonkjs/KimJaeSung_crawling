# 신뢰할 수 있는 연결과 예외 처리
# 페이지를 찾을 수 없는 경우 : 404 에러
# 서버를 찾을 수 없는 경우 : 500 에러

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen('http://www.pythonscraping.com/pages/error.html')
    #html = urlopen('http://www.pythonscraping.com/pages/page1.html') -> 이코드는 작동하기 때문에 It worked! 출력
except HTTPError as e :
    print(e)
except URLError as e :
    print('The server could not be found!')
else:
    print('It worked!')
