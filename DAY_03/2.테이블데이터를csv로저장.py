import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs = BeautifulSoup(html, 'html.parser')

table = bs.find_all('table', {'class':'wikitable'})[0]
rows = table.find_all('tr')

csvFile = open('editors.csv', 'wt', encoding='utf-8')
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = [] # 리스트 초기화
        for cell in row.find_all(['th', 'td']):
            print(cell.text.strip())
            csvRow.append(cell.text.strip()) # 한행의 정보를 리스트에 추가
        writer.writerow(csvRow) # 리스트 값을 하나하나 저장
finally:
    csvFile.close()