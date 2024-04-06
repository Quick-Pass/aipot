if __name__ == "__main__": # 모듈이 메인모듈인지 확인한다.
    # 숫자형 자료 출력
    print("정수형 자료 출력 : {}, {}, {}".format(123, -345, 0))
    print("실수형 자료 출력 : {}, {}".format(123.45, -3.45))
    
    # 문자열 자료 출력
    print("Hello?") # 쌍따옴표로 출력하는 문자열이다.
    print('Hello?') # 홑따옴표로 출력하는 문자열이다.

    # 리스트 자료 출력
    print([1, "2", True]) # 숫자, 문자, 불 자료형을 출력하는 리스트이다.

    # 튜플 자료 출력
    print( (1, "2", True) ) # 숫자, 문자, 불 자료형을 출력하는 튜플이다.

    #딕셔너리 자료 출력
    # dict 변수는 딕셔너리 자료형을 선언하는 변수이다.
    dict = { "key1" : "1", "key2" : 2, "key3" : True }

    print(dict) # dict 변수를 출력한다.

    # 집합 자료 출력 - 중복을 허용하지 않는다.
    set1 = set([1, 2, 3]) # 입력한 집합을 set1 변수로 선언한다.
    set2 = set("Hello?") # "Hello?" 입력한 집합을 set2 변수로 선언한다.

    print(set1) # set1 변수를 출력한다.
    print(set2) # set2 변수를 출력한다.

    # 불 자료 출력
    print(True) # 참을 출력한다. True에서 앞글자가 대문자이다.
    print(False) # 거짓을 출력한다. False에서 앞글자가 대문자이다.

