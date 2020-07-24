# Note

**노트 (나중에 정리)**

### Form (input)

```python
<h1>{{ question.question_text }}</h1>

<form action="{% url 'polls:vote' question.id %}"  method="post">
    {% csrf_token %}
    {% for choice in question.choice_set.all %}
        <input type="radio" name="choice" value="{{ choice.id }}">
        {{ choice.choice_text }}
        
    {% endfor %}
    <br>
    <input type="submit" value="투표">
</form>
```





### CSRF

> ```python
> {% csrf_token %}
> ```
>
> > 서버 에서 클라이언트에게 쿠키를 생성할때, 번호를 같이 보내서 다음 액션시 인식
> > 요청1회당 값이 변경된다.
> > 액션없이 주소창에서만 파라미터를 통해 데이터에 접근하려는 경우, 서버에서 차단한다.
>
> >  get방식은 ? 뒤에 값을 붙여 넘긴다.
> > 장고의 기본값은 post 방식일때, CSRF 적용이 가능하다 







---



테이블을 만든적이 없다?

Templates / App명