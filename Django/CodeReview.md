# CodeReview



> 장고걸스 샘플 : https://tutorial.djangogirls.org/ko/django_models/

```python
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
# 모델(객체, object)을 정의하는 코드
# Post : 모델의 이름 (항상 클래스 이름의 첫글자는 대문자로 써야함)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
		
    # 속성정의(author, title, text, created_date, published_date)
    # models.ForeignKey : 다른모델에 대한 링크를 의미
    # models.CharField : 글자수가 제한된 텍스트를 정의할 때 사용, 글제목같이 짧은 문자열 정보를 저장할때 사용
    # models.TextField : 글자수에 제한이 없는 긴 텍스트
    # models.DateTimeField : 날짜와 시간을 의미
    
    def publish(self):
    # publish 메서드(method)
    # 메서드 명은 소문자와, _ 결합으로 사용
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
      
    # __str__을 호출하면 Post모델의 제목텍스트를 얻을수 있다. 

```

