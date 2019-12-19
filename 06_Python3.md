# 06_Python3



### 1. venv 설치 및 실행

```shell
// 디렉토리에 venv 설치하기 
$ python3 -m venv venv

// 가상환경 실행하기(for Mac)
$ source venv/bin/activate

// 가상환경 종료하기
$ deactivate
```



### 2. For 문 샘플

###### 메인.py(Ex. hello.py)

```python
# 메인상단에 작성(고정)
from flask import Flask, escape, request, render_template
import random

app = Flask(__name__)



  
# 샘플 - 원하는 내용작성
@app.route('/[파일명]')
def movies():
    movies = ['조커', '겨울왕국2', '터미네이터', '어벤져스']
    return render_template('[파일명].html', movies = movies)

  
  
  
# 하단에 작성(고정)
if __name__ == "__main__":
    app.run(debug=True)
```

###### HTML (Ex. Movies.html)

```html
{# {% 주석입니다. 랜더템플릿 주석은 HTML랜더(화면에서 보여질때)시 날려버려요 %} #}

{% for movie in movies %}
  {% if movie == '조커' %}
  	<li>{{ movie }} -> 이 영화 진짜 잼있어</li>
  {% elif movie == '겨울왕국2' %}
  	<li>{{ movie }} -> 울라프 귀여워</li>
  {% else %}
  	<li>{{ movie }}</li>
  {% endif %}
{% endfor %}
```



원래 Flask파일은 app.py로 사용해야 한다

