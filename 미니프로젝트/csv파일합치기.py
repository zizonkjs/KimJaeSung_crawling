import pandas as pd


# 각 CSV 파일을 읽어들임
df1 = pd.read_csv('saramin_jobs.csv')
df2 = pd.read_csv('saramin_jobs.csv1')
df3 = pd.read_csv('saramin_jobs.csv2')
df4 = pd.read_csv('saramin_jobs.csv3')

# 데이터프레임을 하나로 합침
df_combined = pd.concat([df1, df2, df3, df4], ignore_index=True)

# 통합된 데이터프레임을 새로운 CSV 파일로 저장
df_combined.to_csv('saramin_jobs_combined.csv', index=False, encoding='utf-8')