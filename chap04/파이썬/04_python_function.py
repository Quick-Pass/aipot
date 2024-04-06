def print_for(): # print_for 함수를 "def" 예약어를 사용해 선언한다.
    # 호출된 함수는 아래 코드를 수행한다.
    result = ['one', 'two', 'three'] # 문자열을 선언한 리스트

    for a in result: # 변수 a를 리스트를 반복하는 요소로 선언한다.
        print(a)

if __name__ == "__main__": # 모듈이 메인모듈인지 확인한다.
    print_for() # print_for 함수를 호출한다.  