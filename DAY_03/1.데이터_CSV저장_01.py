# CSV 파일 저장
# writer = csv.writer(file, delimiter)

# writer : csv writer 객체 리턴

# 파일 저장
# writer.writerow(row or list) : 한라인씩 csv파일에 저장
# writer.writerows(rows) : 여러 라인을 csv파일에 저장

import csv

csvFILE = open('test.csv', 'w', encoding='UTF-8')

try : 
    writer = csv.writer(csvFILE)
    writer.writerow(('number', 'number+2', '(number+2)^2'))

    for i in range(10):
        writer.writerow((i, i+2, pow(i+2,2)))
except Exception as e:
    print(e)
finally:
    csvFILE.close()



