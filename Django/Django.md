# Django



### 기본화면을 로컬서버에 에 띄워보자

1.  프로젝트 기본구조 생성 (폴더 직접 생성하면 큰일남!!)

```shell
$ django-admin startproject [폴더명]
```

2. App 생성

> App 별로, view 와 model을 가질수 있다
>
> App 은 기능별, 카테고리별 작업자 마음데로 그룹핑이 가능하다

```shell
$ django-admin startapp [App명]
```

3. 프로젝트 실행

```shell
$ python manage.py runserver
```



4. 언어 및 시간 설정 변경 

> settings.py 

```python
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
```



6. 페이지 경로 설정하기 	

> urls.py 

```python
from django.contrib import admin
from django.urls import path
from secondapp import views
# from [가져올 App명] import views
# App에서 views(java에서 컨트롤러 개념)를 가져와 사용한다
# from . import views 본인과 같은 경로인경우 . 으로 표현한다
urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.main),
  	# views의 index1 함수를 가져오겠다
]
```

> View.py

```python
from django.shortcuts import render
from django.http import HttpResponse

def main(request):
 return HttpResponse('<h1>main</h1>')
```



7. 데이터 베이스 연결

> settings.py

```python
DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.mysql',
 'NAME': 'django',
 'USER': 'root',
 'PASSWORD': '1234',
 'HOST': 'localhost',
 'PORT': 3306
 }
}
```



8. 모델 내용 반영

```shell
 $ python manage.py makemigrations [App 이름]
```

```shell
$ python manage.py migrate
```



※ 데이터베이스 작업 실패시

1. 데이터베이스 관련 파일 모두 삭제 후 재시도
2. 관련 파일만 삭제 (기존 데이터 유지) 
   - python manage.py makemigrations 
   - python manage.py showmigrations
   - python manage.py migrate -–fake 앱 zero 
   - 마이그레이션 파일 삭제 0001_initial.py 등
   - python manage.py makemigrations
   - python manage.py migrate --fake-initial



---



### Ect.

> 명령어 정리

```shell
# 마이그레이션 파일 생성
$ python3 manage.py makemigrations <app-name>

# 마이그레이션 적용
$ python3 manage.py migrate <app-name>

# 마이그레이션 적용 현황
$ python3 manage.py showmigrations <app-name>

# 지정 마이그레이션의 SQL 내역
$ python3 manage.py sqlmigrate <app-name> <migration-name>
```



> URL 바인딩

```python
from django.contrib import admin
from django.urls import path, include
from firstapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index1/', views.index1),
    path('index2/', views.index2),
    path('first/', include('firstapp.urls')),
]
```



>  프로젝트 관리에 필요한 명령어 사용 가능

- runserver : 서버 실행
- startapp : 앱 생성
- createsuperuser : 관리자 생성
- migrate : 변경사항을 데이터베이스로 반영
- makemigrations app : app의 모델 변경사항 확인
- shell : 쉘을 통해 데이터 확인
- collectstatic : 여러개의 App 에서 사용하는 static 파일을 한 곳으로 모음



---



### Note

setting : 데이터 설정시 중요

database설정 , staticURL설정 - > 기본

