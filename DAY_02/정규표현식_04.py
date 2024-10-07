# 전방 탐색
# 전방 긍정 탐색
# 패턴과 일치하는 문자열을 만나면 패턴 앞의 문자열 반환: (?=패턴)

# 전방 부정 탐색(?!)
# 패턴과 일치하지 않는 문자열을 만나면 패턴 앞의 문자열 반환: (?!패턴)

import re

lookahead1 = re.search('.+(?=won)', '1000 won')
if(lookahead1 != None):
    print(lookahead1.group())
else:
    print('None')

lookahead2 = re.search('.+(?=am)',	'2023-01-26	am	10:00:01')
print(lookahead2.group())

lookahead3 = re.search('\d{4}(?!-)', '010-1234-5678')
print(lookahead3)

print('-'*50)

# 후방 탐색
# ?< 긍정 탐색
# 패턴과 일치하는 문자열을 만나면 패턴 뒤의 문자열 반환

# 후방 ?<! 부정
# 패턴과 일치하지 않는 문자열을 만나면 패턴 뒤의 문자열 반환

lookbehind1 = re.search('(?<=am).+', '2023-01-26	am	11:10:01')
print(lookbehind1)

lookbehind2 = re.search('(?<=:).+',	'USD:	$51')
print(lookbehind2)

# 후방 부정
lookbehind3 = re.search(r'\b(?<!\$)\d+\b',	'I	paid	$30	for	100	apples.')
print(lookbehind3)