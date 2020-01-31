# Django2

1. workbench 에서 새로운 스키마를 생성한다 (python_db)

2. Setting.py 파일에서 데이터 베이스의 네임을 스키마명으로 변경한다

   ```python
   DATABASES = {
     'default': {
       'ENGINE': 'django.db.backends.mysql',
       'NAME': 'python_db',
        # name = 스키마명
       'USER': 'root',
       'PASSWORD': '1234',
       'HOST': 'localhost',
       'PORT': 3306
     }
   }
   ```

3. 뷰 파일을 작성한다 (부를 페이지 명을 작성한다)

   > Views.py = 컨트롤러 역활

   ```python
   from django.http import HttpResponse
   def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
   ```

   

4. 접속주소 URL 을 설정한다

   > 프로젝트 URL = 그냥작성
   >
   > App URL = 프로젝트에 인클루드 해서 바인딩

   ```python
   from django.urls import path
   from . import views
   urlpatterns = [
    path('', views.index, name='index'),
   ]
   ```

   ```python
   urlpatterns = [
    …
    path('polls/', views.index, name='polls'),
   ]
   ```

   

5. 서버를 구동 시킨다

   >  python manage.py runserver

   



---



### Note

> **ForeignKey(외래키)**로 가져오는것은 다른 테이블의 기본키만 가져올 수 있다.
>
> **Model.py**

```python
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # models.ForeignKey : Question 테이블의 아이디를 ForeignKey 로 사용한다 
    # on_delete : 삭제되었을때, 어떻게 동작할 것인가? (CASCADE 되어라 : 데이터도 같이 삭제 되어라)  
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```



> **model**을 작성한뒤, 터미널에서 inspectdb명령어를 실행하면, 쉘에 자동으로 코드가 입력된다

```shell
$ python manage.py inspectdb
```

```python
class Shop(models.Model):
  shop_id = models.AutoField(primary_key=True)
  shop_name = models.CharField(max_length=100, blank=True, null=True)
  shop_desc = models.CharField(max_length=100, blank=True, null=True)
  rest_date = models.CharField(max_length=100, blank=True, null=True)
  parking_info = models.CharField(max_length=100, blank=True, null=True)
  img_path = models.CharField(max_length=255, blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'shop'
    # shop 이라는 테이블을 사용할꺼야.
          
```



Admin.py 에서 관리자 사이트에서 데이터를 관리할 수 있도록 등록















