import pandas as pd
from tabulate import tabulate

hollys=pd.read_csv('hollys_store_info.csv')
hollys_df=pd.DataFrame(hollys)
hollys_df.index = hollys_df.index + 1

# tabulate를 사용하여 출력
print(tabulate(hollys_df, headers='keys', tablefmt='grid', showindex=True))

# 특정 지역에 있는 커피 매장 출력하기
# 무한반복 : quit 입력시 프로그램 종료
# 입력한 지역에 있는 모든 매장의 매장이름, 주소, 전화번호를 검색해서 출력

while True:
    region = input('검색할 지역을 입력하세요(quit 입력시 종료):').strip()
    if region.lower() == 'quit':
        print("종료합니다.")
        break
    # 지역명 검색
    filtered_df = hollys_df[hollys_df['지역'].str.contains(region)]

    if not filtered_df.empty:
        print(f"검색된 매장 수: {len(filtered_df)}")
        print(tabulate(filtered_df[['매장명', '주소', '전화번호']], headers='keys', tablefmt='grid', showindex=True))
    else:
        print(f"{region} 지역에 해당하는 매장을 찾을 수 없습니다.")





# reset_index()
# 를 사용해서 인덱스 값초기화

    

    





