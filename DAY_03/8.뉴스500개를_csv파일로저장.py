import urllib.request
import datetime
import json
import datetime
import pandas as pd
import urllib.request
import datetime
import json
import pandas as pd

def get_request_url(url):
    client_id = "vOV6XbhT8WhoMoXeCFIR"
    client_secret = "y2sUZHpOle"

    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print(f"Error for URL: {url}")
        return None

def get_naver_search(node, search_text, start, display):
    base = "https://openapi.naver.com/v1/search"
    node = f"/{node}.json"
    query_string = f"{urllib.parse.quote(search_text)}"

    parameters = "?query={}&start={}&display={}".format(query_string, start, display)

    url = base + node + parameters
    response = get_request_url(url)

    if response is None:
        return None
    else:
        return json.loads(response)

def main():
    node = 'blog'  # 검색할 카테고리 (blog)
    search_text = 'IT개발 데이터 채용공고'
    cnt = 0
    json_result_list = []

    # 100개씩 5번 호출하여 500개 데이터 수집
    for start in range(1, 500, 100):
        json_response = get_naver_search(node, search_text, start, 100)
        if (json_response is not None) and (json_response['display'] != 0):
            for post in json_response['items']:
                cnt += 1
                result = {
                    "count": cnt,
                    "date": post['postdate'],
                    "title": post['title'],
                    "description": post['description'],
                    "org_link": post['link'],
                    "link": post['link']
                }
                json_result_list.append(result)

    # DataFrame 생성 및 CSV 파일로 저장
    columns = ['count', 'date', 'title', 'description', 'org_link', 'link']
    result_df = pd.DataFrame(json_result_list, columns=columns)
    result_df.to_csv(f'{search_text}_naver_{node}.csv', index=False, encoding='utf-8')
    print(f"CSV 파일로 저장되었습니다: {search_text}_naver_{node}.csv")

if __name__ == '__main__':
    main()