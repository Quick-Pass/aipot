import json
import urllib.request # 사용할 패키지(모듈)는 
                      # 가장 먼저 실행되어야 하므로
                      # 파일 내용의 가장 위에 작성한다.

if __name__ == "__main__": # 모듈이 메인모듈인지 확인한다.
    print("urllib 네트워크 모듈을 사용한다.")

    url = "https://jsonplaceholder.typicode.com/posts" # 데이터를 요청하는 URL 주소

    request = urllib.request.Request(url) # 요청 객체를 생성한다.
    response = urllib.request.urlopen(request) # URL 주소로 데이터를 요청한다.
    rescode = response.getcode() # 응답이 어떠한지 코드를 물어본다.

    if rescode == 200 : # 응답이 정상일 때 들여쓰기 된 코드들을 실행한다.
        response_body = response.read() # 응답 결과를 읽는다.

        obj = json.loads(response_body.decode('utf-8')) # 응답을 JSON 객체로 감싼다.
        print("응답 결과 : {}".format(obj))
    else: # 응답이 정상이 아닐 때 들여쓰기 된 코드들을 실행한다.
        print("응답 오류입니다. code : {}".format(rescode))

