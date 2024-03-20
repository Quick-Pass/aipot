import json
import openai
import urllib.request
import requests

# pip 패키지 설치 후 아래의 코드를 추가
import base64
import io
import cv2
import numpy as np
from PIL import Image

def translate_contents(text):
    # 네이버 클라우드에서 서비스를 신청하여 발급받은 Client ID 값
    client_id = ""

    # 네이버 클라우드에서 서비스를 신청하여 발급받은 Client Secret 값
    client_secret = ""

    encText = urllib.parse.quote(text)

    data = "source=en&target=ko&text=" + encText
    url = "https://naveropenapi.apigw.ntruss.com/nmt/v1/translation"

    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID", client_id)
    request.add_header("X-NCP-APIGW-API-KEY", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    return_contents = ""

    if(rescode==200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        obj = json.loads(response_body.decode('utf-8'))
        return_contents = obj['message']['result']['translatedText']
    else:
        return_contents = text

    return return_contents

def main() :
    api_key = open("api-key.txt").read().strip()
    openai.api_key = api_key

    arr_resp_contents = []

    for chunk in openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=[{
                "role": "user",
                "content" : "\
Tell me 5 person who said a various Quotes\
And tell me the prompts in English to draw a picture that matches each quote.\
The format you are informing us of is as follows. (remove 'Midjourney prompt:' !) :\
{{Life Quote}}\
- {{Quoter}}\
{{Please write a quote in English in an emotional tone and poetic writing style, and express it in short words like an midjourney prompt}}"
            }],
            stream=True,
    ):
        content = chunk["choices"][0].get("delta", {}).get("content")
        if content is not None:
            arr_resp_contents.append(content)
            # print(content, end='')

    resp_contents = "".join(arr_resp_contents)
    resp_contents = resp_contents.replace("\n\n", "\n").replace("Life Quote: ", "")\
        .replace("Midjourney prompt: ", " - ").replace("Midjourney Prompt: ", " - ")\
        .replace("\n- Prompt: ", " - ").replace("\nPrompt: ", " - ").replace("\n- prompt: ", " - ")\
        .replace("\n- ", " - ").replace("\n - ", " - ").replace("\n     - ", "")\
        .replace("\n    - ", "").replace("\n-  - ", " - ").replace("\n-  - ", " - ")
    print(resp_contents)

    # '''
    arr_wise_sayings = resp_contents.split("\n")

    count = 0
    for ws in arr_wise_sayings:
        if ws.strip() != "":
            count = count + 1
            print(ws)

            arr_sayings = ws.split(" - ")
            wise_say = ""

            if "Life Quote {}: ".format(count) in arr_sayings[0]:
                wise_say = arr_sayings[0].replace("Life Quote {}: ".format(count), "")

            if ". " in arr_sayings[0]:
                wise_say = arr_sayings[0].split(". ")[1].replace("\"", "")
            elif ") \"" in arr_sayings[0]:
                wise_say = arr_sayings[0].split(") \"")[1].replace("\"", "")
            else:
                wise_say = arr_sayings[0].replace("\"", "")

            speaker = arr_sayings[1]
            prompt = arr_sayings[2]

            print(speaker, wise_say, prompt)

            translated_wise_say = translate_contents(wise_say)
            translated_speakers = translate_contents(speaker)

            # Stable Diffusion 에서 API 호출 시 필요한 파라미터
            image_generate_parameter = {
                "prompt": "((Masterpiece, 4K UHD, highres))\n{} --ar 1:1".format(prompt),
                "negative_prompt": "easynegative, NSFW, text, television, watermark, ng_deepnegative_v1_75t, paintings, sketches, (low quality:2), (normal quality:2), (worst quality:2), lowres, ((monochrome)), ((grayscale)), acnes, skin spots, age spot, skin blemishes, bad feet, ((wrong feet)), (wrong shoes), bad hands, distorted, blurry, missing fingers, multiple feet, bad knees, extra fingers, multiple bodies, multiple heads, multiple legs, multiple hands, deformed hands",
                "width": 512,
                "height": 512,
                'override_settings': {
                    'sd_model_checkpoint' : "v1-5-pruned-emaonly",
                    'sd_vae' : "vae-ft-mse-840000-ema-pruned (1).safetensors",
                    'sd_lora': None,
                    'sd_checkpoint_hash' : "6ce0161689b3853acaa03779ec93eafe75a02f4ced659bee03f50797806fa2fa",
                },
                "enable_hr": False,
                "denoising_strength": 0.7,
                "firstphase_width": 0,
                "firstphase_height": 0,
                "hr_scale": 2,
                "hr_upscaler": "R-ESRGAN 4x+ Anime6B",
                "hr_second_pass_steps": 0,
                "hr_resize_x": 0,
                "hr_resize_y": 0,
                "styles": ["string"],
                "seed": -1,
                "subseed": -1,
                "subseed_strength": 0,
                "seed_resize_from_h": -1,
                "seed_resize_from_w": -1,
                "batch_size": 1,
                "n_iter": 1,
                "steps": 40,
                "cfg_scale": 7,
                "restore_faces": False,
                "tiling": False,
                "eta": 0,
                "s_churn": 0,
                "s_tmax": 0,
                "s_tmin": 0,
                "s_noise": 1,
                "override_settings_restore_afterwards": True,
                "script_args": [],
                "sampler_index": "DPM++ 2M Karras",
                "scripts": None
            }

            # Stable Diffusion API 주소로 파라미터를 같이 전달하여 호출한다.
            resp = requests.post("http://localhost:7860/sdapi/v1/txt2img", json=image_generate_parameter)
            json_obj = resp.json()
            
            # base64 형태로 생성된 이미지 데이터를 변수에 넣음
            base64_img_str = json_obj['images'][0]
            print(translated_wise_say, translated_speakers)

            # 명언을 저장하는 코드
            file = open("result/{}.txt".format(speaker), "w", encoding="utf-8")
            file.write("영문 명언을 말한 사람 : {}\n".format(speaker))
            file.write("영문 명언 : {}\n\n".format(wise_say))
            file.write("한글 번역 명언을 말한 사람 : {}\n".format(translated_speakers))
            file.write("한글 번역 명언 : {}\n".format(translated_wise_say))
            file.write("이미지를 생성하기 위한 프롬프트 : {}".format(prompt))
            file.close()

            # Stable Diffusion API를 통해 생성된 이미지데이터를 이미지 파일로 저장하는 코드
            imgdata = base64.b64decode(base64_img_str)
            img_out = Image.open(io.BytesIO(imgdata))
            img_out = np.array(img_out)
            img_out = cv2.cvtColor(img_out, cv2.COLOR_BGR2RGB)

            cv2.imwrite('result/{}.png'.format(speaker), img_out)
    # '''

if __name__ == "__main__":
    main()

