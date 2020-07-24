# Models

자동으로 데이터 베이스를 만들어 줌

데이터 테이블과 속성이 같아야 한다

모델을 사용하기 위해서는 setting.py 파일에서 앱명을 입력을 해주야 한다





**가장 많이 사용하는 모델 클래스 속성**

CharField : 제한된 문자열 타입, max_length 옵션으로 최대 입력 길이 지정

IntegerField : 정수 타입

DateTimeField : 날짜 / 시간 타입 (models.Model):파이썬의 datetime.datetime)





### 모델함수

1. 모델클래스.objects.all(models.Model)

   데이터 전체 조회

2. 모델클래스.objects.get(models.Model):속성=검색어)

   특정조건의 것

3. 모델클래스.objects.filter(models.Model):속성=검색어)

   특정 조건으로 여러개





### 모델관계

나중에 공부

