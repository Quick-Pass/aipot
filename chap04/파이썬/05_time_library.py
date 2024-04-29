import time # 사용할 패키지(모듈)는 가장 먼저 실행되어야 하므로 파일 내용의 가장 위에 작성한다.

if __name__ == "__main__": # 모듈이 메인모듈인지 확인한다.
    print("time 모듈을 사용한다.")

    now = time.time() # 현재 시간을 유닉스 타임스탬프로 가져온다.   
    readable_time = time.ctime(now) # 유닉스 타임스탬프를 읽을 수 있는 형태로 변환합니다.

    print("현재 시간:", readable_time)