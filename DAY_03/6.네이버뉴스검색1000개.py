import urllib.request
import datetime
import json

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
    node = 'blog'  # 변경된 부분
    search_text = 'IT개발 데이터 채용공고'
    cnt = 0

    json_response = get_naver_search(node, search_text, 1, 500)
    if (json_response is not None) and (json_response['display'] != 0):
        for post in json_response['items']:
            cnt += 1

            print(f"[{cnt}]", end=" ")
            print(post['title'])
            print(post['description'])
            print(post['bloggername'])  # 블로그에서는 bloggername을 출력
            print(post['link'])
            print(post['postdate'])

if __name__ == '__main__':
    main()
