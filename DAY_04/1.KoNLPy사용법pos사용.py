# 한글 자연어 처리 라이브러리 KoNLPy
# 크롤링 및 wordcloud 생성

# morphs
# 텍스트에서 형태소를 반환

# nouns
# 텍스트에서 명사만 반환

# phrases
# 텍스트에서 어절을 반환

#pos
# 텍스트에서 품사 정보를 부착하여 반환
# 각 형태소를 품사와 함께 리스트로 반환

#pos 품사 사용
from konlpy.tag import Okt

# norm -> 정규화 True(문법맞춰줌), False(그대로 출력)
# stem -> 단어의 어간을 리턴 True(맞춰줌), False(그대로출력)

# Okt.pos -> list 형태로 출력함.
okt = Okt() # Open korea text 줄임말
text = "마음에 꽂힌 칼한자루 보다 마음에 꽂힌 꽃한송이가 더 아파서 잠이 오지 않는다"

okt_tags = okt.pos(text, norm=True, stem=True)
print(okt_tags)

okt_nouns = okt.nouns(text)
print(okt_nouns)
