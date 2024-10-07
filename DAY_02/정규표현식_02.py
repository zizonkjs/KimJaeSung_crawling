# 정규 표현식 findall() 함수

# 일치하는 모든 문자열을 리스트로 리턴
import re
p = re.compile('[a-z]+')

print(p.findall('life is too short! Regular expression test'))

print()

#search 함수
# 일치하는 첫 번째 문자열만 리턴
result = p.search('I like apple 123')
print(result)

result = p.findall('I like apple 123')
print(result)



