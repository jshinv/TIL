# App셋팅하기

apmall

1. 앱을 만든다

   ```shell
   $ django-admin startapp [폴더명]
   ```

2. 앱안에 urls.py 파일을 만든다

   > 앱에 접근했을때, 사용할 URL 주소를 셋팅한다

   ```python
   from django.urls import path
   from . import views
   
   urlpatterns = [
     path('/', views.index),
   ]
   ```

3. 앱에 셋팅한 URL을 사용할수 있게 하기 위해서는

   > 앱세 셋팅한 URL을 사용하기 위해서는 메인 urls.py에서 연결을 시켜줘야 한다

   ```python
   from django.contrib import admin
   from django.urls import path, include
   from common import views
   from cjmall import views
   from glowpick import views
   from gsshop import views
   from apmall import views
   
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('index/', views.index),
       path('shop/', include('common.urls')),
       path('shop/cjmall', include('cjmall.urls')),
       path('shop/glowpick', include('glowpick.urls')),
       path('shop/gsshop', include('gsshop.urls')),
       path('shop/apmall', include('apmall.urls')),
   ]
   ```

   

4. 앱에 있는 views.py 파일에 urls.py에서 셋팅한 index를 어떤 호출시 변환해줄건지 셋팅한다

   ```python
   from django.shortcuts import render
   from django.http import HttpResponse
   
   def index(request):
       return render(
           request, 'apmall/index.html', { } )
   ```

   

5. 위의 경로대로 templates폴더아래 앱템플릿 폴더를 생성한다







---

### Ect

- 파일 인클루드

  {% include 'common/sidebar.html' %}

