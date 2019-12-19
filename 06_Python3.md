# 06_Python3



### 1. venv

```shell
// 디렉토리에 venv 설치하기 
$ python3 -m venv venv

// 가상환경 실행하기
$ source venv/bin/activate

// 가상환경 종료하기
$ deactivate
```



### 2. Flask sample

```python
# 상단필수 적용 
from flask import Flask, render_template, request

app = Flask(__name__)

# 개별 작성
@app.route('/ping')
def ping():
    return render_template('ping.html')


# 하단필수적용
if __name__ == "__main__":
    app.run(debug=True)
```

