# AI 프롬프트 활용능력(AI·POT, 아·이·팟) 실습 자료실입니다.
## 프롬프트 파이프라인 실습자료
### 프롬프트 파이프라인 실습자료를 실행하기 위해서 사전에 작업이 필요합니다.
### 아래의 코드를 실행하여 설정을 완료해 주세요.

```
(윈도우 CMD 기준으로 파이썬 가상 환경이 설정 안되어 있을 때 설정하는 방법입니다.)
(만약 CMD를 실행했을 때 위치가 c 드라이브이고, git에서 받은 프로젝트도 c드라이브에 위치할 경우)
C:\Users\~~~> cd C:\~~~~\aipot\chap04\prompt_pipeline

 
(만약 CMD를 실행했을 때 위치가 c 드라이브이고, git에서 받은 프로젝트가 d드라이브에 위치할 경우)
C:\Users\~~~> d: 
d:> cd d:\~~~~\aipot\chap04\prompt_pipeline
```

### 디렉토리를 이동한 후 다음 명령어를 실행합니다.
```
python3.exe -m venv venv

cd venv/scripts
activate.bat

cd .. (scripts 폴더에서 빠져나옴, 위치는 venv 폴더가 됨)
cd .. (venv 폴더에서 빠져나옴, 위치는 프로젝트 메인 폴더가 됨)

pip install -r requirements.txt
```
### 또한 코드를 실행하기 위해서는 아래와 같은 API 키 정보가 필요합니다.
<ul>
<li>네이버 클라우드에서 파파고 API 키 발급받기</li>
<li>OpenAI의 ChatGPT API 키 발급받기(api-key.txt 파일로 저장하기)</li>
</ul> 

### 그리고 Stable Diffusion을 API 기능을 사용하도록 활성화 하여 실행을 한 상태에서 아래의 코드를 실행하면 구동됩니다.
```
(파이썬 코드 실행하기)
python prompt_process.py

※ 도서 내용 중에 해당 챕터 안에 실습자료가 없거나 잘못된 부분은 카페로 제보 해 주세요.
```




[대한민국 최고의 인공지능 프롬프트 자격증 퀵패스 - AI 프롬프트 활용능력(AI·POT, 아·이·팟) 카페](https://cafe.naver.com/quickpass)<br>
(컨트롤 키를 누르고 링크를 누르면 새 창으로 열립니다)