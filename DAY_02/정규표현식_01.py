# 정규 표현식
# 특정한 규칙을 가진 문자열의 집합을 표현하는데 사용하는 형식 언어

# 정규 표현식 사용
# 문자열과 관련된 문제 해결을 위해 사용
# 문자열 치환, 검색, 추출 등
# 문자열의 유효성 검사
# email 주소, 전화번호, 웹사이트 주소 등

#장점 
# 다양한 입력 문자열 처리가 간결
# 범용성 : 다양한 프로그래밍 언어에서 지원
# 생산성 향상

#단점
#정규 표현식 자체의 어려움
#소스 코드가 어려워짐

# 정규표현식 기호 : 문자집합
# ^ : 문자열의 시작
# $ : 문자열의 끝나는지점 검사
# . : 임의의 한 문자 -> 많이 사용
# \b : 단어의 경계 검색
# \s : 공백문자
# \S :  공백 문자가 아닌 나머지 문자 \s의 not
# \w : 알파벳, 숫자, _ 를 검색
# \W : 알파벳, 숫자, _를 제외한 문자 \w의 not
# \d : 숫자와 동일(digit)
# \D : 숫자를 제외한 모든 문자 \d 의 not
# \ : 확장문자, 역 슬래시 다음에 일반 문자가 오면 특수 문자로 취급
#     역 슬래시 다음에 특수 문자가 따라오면 그 문자 자체를 의미
#     \\* 는 * 자체를 의미
# r'패턴' : 컴파일 할 정규식이 순수 문자열임을 알림 (raw string)
#           역슬래시를 1번만 사용하여 '\' 문자 자체릂 표현하기 위함

# [] : 문자의 집합이나 범위. 두 문자 사이에는 '-' 기호로 범위를 지정 -> 많이사용
# [^] : []의 not [^abc] : abc 제외
# () : 소괄호 안의 문자를 하나의 문자로 인식(그룹) -> 많이 사용
# | : or 연산
# (?i) : 대소문자 구분하지 않음
# (?:) : 뒤에 따라 나오는 문자들을 하나의 그룹으로 합침
# ?=(regex) : 정규식과 일치하는 문자열을 만나면 그 정규식 앞의 값을 반환
#             '='은 긍정을 의미
# ?<=(regex) : 후방 긍정 검색
# ?!(regex) : 전방 부정(!) 탐색 일치하는 패턴이 없으면 전방(앞에걸) 가져옴
# ?<!(regex) :  후방 부정(!) 탐색 일치하는 패턴이 없으면 후방(뒤에걸) 가져옴

# 수량 표시
# * : 앞 문자가 없을 수도 있고 무한정 많을 수도 있음 : (zero or more) -> X*(많이 사용)
# + : 앞 문자가 하나이상 : (one or more) -> x+(많이사용)
# ? : 앞 문자가 없거나 한개 있음 : (zero or one) -> 1?
# {n} : 정확히 n개 -> x{n}
# {n,} : 최소 n개 -> x{n,}
# {n,m} : n이상 m이하
# *? : 가장 적게 일치하는 패턴 검색

# 자주 사용하는 정규 표현식
# 숫자 : [0-9]*$
# 영문자 : [a-zA-Z]*
# 한글 : [가-힣]*
# 영문자와 숫자 : [a-zA-Z0-9]*
# 이메일 : [a-zA-Z0-9]+@[a-zA-Z0-9]+
# 휴대전화 : (01(?:0|1|[6-9]))-(\d{3,4})-(\d{4})
# 일반전화 : (\d{2,3})-(\d{3,4})-(\d{4})
# 주민번호 : (\d{6})[-][1-4](\d{6})
# IP 주소 : ([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})
# 패스워드 : ^[a-z0-9_-]{6,18}
#           소문자, 숫자, _, - 포함하여 6글자 이상 18글자 이하

# 정규표현식 re 모듈 함수
# compile(pattern, flags=0) : pattern을 이용하여 정규식 객체를 반환
#                             패턴을 여러 번 사용할 경우, compile()함수를 이용하여 객체 생성
# search(pattern, string) : 문자열 전체를 검색하여 pattern이 존재하는지 검색
#                           처음 매칭되는 문자열 리턴
# match(pattern, stirng) : string의 처음부터 pattern이 존재하는지 검사 ->문장 처음부터 맞는지 체크
#                          공백이 있는 경우가 패턴이 존재하는 경우 검색하지 못함
#                          문장 처음부터 패턴과 일치하는 문자열만 검색
# split(pattern, stirng) : pattern을 구분자로 string을 분리해서 리스트로 반환
# findall(pattern, stirng) : stirng에서 pattern과 매치되는 모든 경우를 찾아 리스트로 반환
# finditer(pattern, stirng) : string에서 pattern과 매치되는 문자열을 반복 가능한 객체로 반환
# sub(pattern, stirng) : string에서 pattern과 일치하는 부분을 repl로 교체한 문자열반환
# subn(pattern, stirng) : sub()와 동일, 결과로 (결과 문자열, 매칭 횟수)를 튜플로 반환
# excape(pattern, stirng) : 영문자 , 숫자가 아닌 문자에 대해 백슬래시 문자를 추가

# 정규 표현식 예제
# 정규 표현식 객체 사용
# 정규식 객체를 생성 : compile(pattern)
# 동일 패턴을 여러 번 검색하는 경우 편리하게 사용
# re 모듈 함수들은 pattern 파라미터 없이 호출이 가능
# search(string, pos), match(string, pos) 등

import re

m = re.match('[a-z]+', 'Python')
print( m ) # -> 소문자가 아닌 대문자가 나와서 검사안함
print(re.search('apple', 'I like apple!'))

print()

# compile( ) 사용 : 객체 생성
p = re.compile('[a-z]+')
m = p.match('python')
print(m)
print(p.search('I like apple 123'))

print()

# match() : 문자열의 처음부터 검사
m = re.match('[a-z]+', 'pythoN') # 소문자가 1개이상
print(m)

m = re.match('[a-z]+', 'PYthon')
print(m)

print()

print(re.match('[a-z]+', 'regex python'))
print(re.match('[a-z]+', ' regexpython'))

print()

print(re.match('[a-z]+', 'regexPython'))
print(re.match('[a-z]+$', 'regexpython'))