# 정규 표현식 : Match 객체 메소드

#Match 객체

#group([group1, ...]) : 매치된 문자열 중 인덱스에 해당하는 문자열을 반환
#                       group(0) 또는 group() : 전체 매칭 문자열 반환
# groups() : 매칭된 결과를 튜플 형태로 반환
# groupdict() : 매칭 결과를 사전(dict) 형태로 반환
# start([group]) : 매칭된 결과 문자열의 시작 위치를 반환
# end([group]) : 매칭된 문자열의 끝 위치를 반환
# span() : 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 반환

# match 메소드 예제
# 전화번호 분석
# 전화번호 : 지역번호 - 국번 - 전화번호
# 전화번호 : (2, 3자리) - (3, 4 자리) - (4자리)
# groups() : 매칭되는 문자열의 전체 그룹을 리턴
import re

tel_checker = re.compile(r'^(\d{2,3})-(\d{3,4})-(\d{4})$')
# \d 숫자 2이상 3이하 개 - 3이상 4이하 개- 4개

print(tel_checker.match('02-123-4567'))
match_groups = tel_checker.match('02-123-4567').groups() #-> 튜플형태로 리턴
print(match_groups)

print(tel_checker.match('053-950-45678')) # 마지막 숫자의 자리수 안맞음
print(tel_checker.match('053950-4567')) # '-' 가 없음

print('-'*50)

# 전화번호에서 - 제거하고 검사하기
tel_number='053-950-4567'
tel_number = tel_number.replace('-', '')
print(tel_number)

tel_checker1 = re.compile(r'^(\d{2,3})(\d{3,4})(\d{4})$')
print(tel_checker1.match(tel_number))
print(tel_checker1.match('0239501234'))

print('-'*50)

# groups()
# 매칭 결과를 튜플로 출력
# group()
# 매칭된 전체 문자열 반환
# group(index)
# 해당 인덱스에 매칭된 문자열 반환
# index = 0 : 전체 리턴
tel_checker2 = re.compile('^(\d{2,3})-(\d{3,4})-(\d{4})$')
m = tel_checker2.match('02-123-4567')

print(m.groups())
print('group():' , m.group())
print('group(0):', m.group(0))
print('group(1):', m.group(1))
print('group(2,3):', m.group(2,3))
print('start():', m.start())
print('end():', m.end())

# 메소드 예제 3

# 휴대전화번호 구성 : 사업자번호(3자리) 국번(3,4), 전화번호 (4)

cell_phone = re.compile('^(01(?:0|1|[6-9]))-(\d{3,4})-(\d{4})$')

print(cell_phone.match('010-123-4567'))
print(cell_phone.match('019-1234-5678'))
print(cell_phone.match('001-123-4567'))
print(cell_phone.match('010-1234567'))