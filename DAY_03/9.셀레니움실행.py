from selenium import webdriver # 웹드라이브사용가능
import time
'''
    selenium 4.xx 버전은 chromedriver 별도 다운로드 할 필요 없음
    - selenium 4.23.1
'''

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

print(driver.title)
print(driver.page_source)
time.sleep(2)
driver.quit()

# page_source -> 웹 브라우저에 보이는 HTML을 모두 가져옴.
