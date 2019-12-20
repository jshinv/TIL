# Telegram



### 1. Bot 만들기

1. 텔레그램 검색창에서 BotFather 검색 

2. 메시지 창에 /newbot 입력

3. 메시지 창에 봇 이름 입력 [이름뒤에는 bot 꼭 붙여줘야함]

4. 샘플 : foruuubot

   [Telegram bots API](https://core.telegram.org/bots/api)



---



### 2. Telegram Making request

`https://api.telegram.org/bot`  <token>/METHOD_NAME



### .env

```html
CHAT_ID ="개인텔레그램 계정 ID"
TELEGRAM_BOT_TOKEN="봇 생성시 만들어진 API키"
```

###### 내 Chat_id 확인방법

`https://api.telegram.org/bot1040763650:AAG74epvwTb5PyBP-AHbd8q60WFBsrNGre8/getupdates`



### 3. 샘플.py

```python
from flask import Flask, render_template, request
from decouple import config
import requests


app = Flask(__name__)

token = config('TELEGRAM_BOT_TOKEN')
# 누구에게 보낼것인가? (chat_id)
chat_id = config('CHAT_ID')
url = "https://api.telegram.org/bot"

@app.route('/')
def hello():
    return "Hello World"

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    text = request.args.get('text')
    requests.get(f'{url}{token}/sendMessage?chat_id={chat_id}&text={text}')
    return render_template('send.html')


@app.route(f'/{token}', methods=["POST"])
def telegram():
    # chat_id = request.get_json[][][]
    return "ok", 200


if __name__ == "__main__":
    app.run(debug=True)
```



---



### 4. WebHook

​	[https://ngrok.com/](https://ngrok.com/)

pythonanywhere 사용 : 로컬 파일은 변경시에만 터미널에서 한번씩 돌려주면 된다.