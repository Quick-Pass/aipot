import json
import urllib.request # 사용할 패키지(모듈)는 가장 먼저 실행되어야 하므로 파일 내용의 가장 위에 작성한다.
import base64         # base64를 처리하는 패키지이다.
import io             # 파이썬에서 기본 입출력을 담당하는 패키지이다.
from PIL import Image # 파이썬에서 이미지를 처리하는 패키지이다.

def save_sd_image(image_obj): # 스테이블 디퓨전에서 생성한 이미지를 저장하는 함수
    base64_img_str = image_obj['images'][0] # 이미지 데이터를 변수에 대입한다.

    image_data = base64.b64decode(base64_img_str) # BASE64 문자열을 해독한다.
    image = Image.open(io.BytesIO(image_data)) # 이미지 데이터를 변수에 대입한다.
    image.save("image.png") # image.png로 저장한다.

if __name__ == "__main__": # 모듈이 메인모듈인지 확인한다.
    host = "http://127.0.0.1:7860" # 스테이블 디퓨전의 로컬 URL 주소
    end_point = "sdapi/v1/txt2img" # 
    
    url = "{}/{}".format(host, end_point) # url의 주소는 "http://127.0.0.1:7860/sdapi/v1/txt2img"이 된다.
    print(url)

    prompt = "fairy in an enchanted forest" # 이미지를 그릴 프롬프트
    negative_prompt = "lowres, ugly face, poor hand, bended fingers" # 네거티브 프롬프트
    image_generate_parameter = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "width": 360, # 이미지를 그릴 너비
        "height": 480, # 이미지를 그릴 높이
        'override_settings': {
            'sd_model_checkpoint' : "v1-5-pruned-emaonly", # 이미지를 생성할 모델 이름
            'sd_lora' : None, # 이미지를 생성할 로라(LoRA) 모델 이름 지정
        },
        "steps": 20, # 이미지를 생성하는데 반복하는 횟수(=Sampling steps)
        "sampler_index": "DPM++ 2M Karras", # 이미지를 그리는 방법(=Sampling methods)
        "n_iter": 1, # 이미지를 생성하는 반복 횟수를 지정(=Batch count)
        "batch_size": 1, # 한 번에 생성하는 이미지의 갯수를 지정(=Batch size)
        "seed": -1,        
        "cfg_scale": 7,
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
        "subseed": -1,
        "subseed_strength": 0,
        "seed_resize_from_h": -1,
        "seed_resize_from_w": -1,
        "restore_faces": False,
        "tiling": False,
        "eta": 0,
        "s_churn": 0,
        "s_tmax": 0,
        "s_tmin": 0,
        "s_noise": 1,
        "override_settings_restore_afterwards": True,
        "script_args": [],
        "scripts": None
    }

    print(image_generate_parameter)

    request = urllib.request.Request(
        url, # 스테이블 디퓨전의 API 호출 URL 주소를 지정한다.
        headers = {'Content-Type': 'application/json'},
        data = json.dumps(
            image_generate_parameter
        ).encode("utf-8"), # 이미지를 생성할 데이터
    ) # 요청 객체를 생성한다.

    response = urllib.request.urlopen(request) # URL 주소로 데이터를 요청한다.
    rescode = response.getcode() # 응답이 어떠한지 코드를 물어본다.

    if rescode == 200 : # 응답이 정상일 때 들여쓰기 된 코드들을 실행한다.
        res_body = response.read() # 응답 결과를 읽는다.
        obj = json.loads(res_body.decode('utf-8')) # 응답을 JSON 객체로 감싼다.
        print("응답 결과 : {}".format(obj))

        save_sd_image(obj) # 이미지를 저장하는 함수이다. 스테이블 디퓨전이 생성한 데이터를 매개변수로 전달한다.
    else: # 응답이 정상이 아닐 때 들여쓰기 된 코드들을 실행한다.
        print("응답 오류입니다. code : {}".format(rescode))
