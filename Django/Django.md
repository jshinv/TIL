# Django



### 기본화면을 로컬에 띄워보자

1.  프로젝트 기본구조 생성 (폴더 직접 생성하면 큰일남!!)

   ```shell
   $ django-admin startproject [폴더명]
   ```

2. App 생성

   - App 별로, view 와 model을 가질수 있다
   - App 은 기능별, 카테고리별 작업자 마음데로 그룹핑이 가능하다

   ```shell
   $ django-admin startapp [App명]
   ```

4. 프로젝트 실행

   ```shell
   $ python manage.py runserver
   ```

5. 언어 및 시간 설정 변경 

- settings.py 

  ```python
  LANGUAGE_CODE = 'ko-kr'
  TIME_ZONE = 'Asia/Seoul'
  ```



6. 페이지 경로 설정하기 

- urls.py 

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

- View.py

  ```python
  from django.shortcuts import render
  from django.http import HttpResponse
  
  def main(request):
   return HttpResponse('<h1>main</h1>')
  ```

  

---



setting : 데이터 설정시 중요

database설정 , staticURL설정 - > 기본

