from openai import OpenAI # 사용할 패키지(모듈)는 
                          # 가장 먼저 실행되어야 하므로
                          # 파일 내용의 가장 위에 작성한다.

if __name__ == "__main__": # 모듈이 메인모듈인지 확인한다.
    print("ChatGPT API를 통해 프롬프트 엔지니어링 수행")

    txt_prompt = "제주도 2박 3일 여행계획을 세워줘"
    print("질의할 프롬프트 : {}".format(txt_prompt))

    client = OpenAI(api_key = "이 곳에 ChatGPT API 키를 입력해주세요.")

    completion = client.chat.completions.create(
        model="gpt-4", # GPT-4 모델을 사용한다.
        messages=[
            {
                "role": "user", # 역할은 사용자로 설정한다
                "content": txt_prompt, # 질의할 내용(프롬프트)을 설정한다.
            }
        ],
    )

    # 챗GPT가 응답한 메시지를 출력한다.
    print("챗GPT가 응답한 내용 : {}".format(completion.choices[0].message.content))

