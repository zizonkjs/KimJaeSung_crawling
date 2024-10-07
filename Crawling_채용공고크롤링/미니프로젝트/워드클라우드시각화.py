import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

font_path = 'c:/Windows/Fonts/malgun.ttf'

import platform
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

# 데이터프레임 로드 (예시로 사용)
df = pd.read_csv('saramin_jobs_combined.csv')

# 텍스트 데이터 추출
text_data = ' '.join(df['Job Sector'].dropna().astype(str).tolist())

# 운영체제에 따른 폰트 경로 설정
if platform.system() == 'Windows':
    font_path = r'c:\Windows\Fonts\malgun.ttf'
elif platform.system() == 'Darwin':
    font_path = r'/System/Library/Fonts/AppleGothic'
else:
    font_path = r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'

# 워드클라우드 생성
wordcloud = WordCloud(font_path=font_path, background_color="white").generate(text_data)

# 워드클라우드 시각화
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()