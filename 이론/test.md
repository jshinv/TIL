##### Bumpy pandas



넘파이 배열

연속적 배열로 한번에 연산이 이루어 진다. 



Pandas array속성

1. 모양에 대한 속성(dim, shape)

2. 데이터 전체 길이 size
3. 타입 :  .dtype 등 



indexing

arr.shap = l , m , n 

arr[i:, :, j, :]

[http://localhost:8888/notebooks/work/jshinv/M_study/%E1%84%92%E1%85%AA%E1%86%A8%E1%84%85%E1%85%B2%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%90%E1%85%A9%E1%86%BC%E1%84%80%E1%85%A8/ch04.NumPy_Basic.ipynb](http://localhost:8888/notebooks/work/jshinv/M_study/확률과 통계/ch04.NumPy_Basic.ipynb)





summury(R)  / discribe(판다스)

series

- 여러게 모이면 데이터 프레임을 구성해 준다

- 로우네임을 갖는다

  ( 시리즈 이름 : index / 값 :  index_value /  같은 d타입으로 구성되어있다. numpy + index | numpy + schema )

- 결측치 제거 : dropna (R은 na.omit)

- 데이터에서 1 : 1 변환 -> transform

- 시리즈에서 1:1 변환 -> map

- 인덱스 변환해주는 여러가지 함수

  (초기화 : reset_index , 특정한 인덱스로 설정 : Set_index)

- 인덱스 와이드를 롱으로 :  malt (인덱스가 늘어난다)

- 인덱스 롱을 와이드로 : pivot ()

- 실습문제 : Tipsdata의 Tiprate =  (tip / total) = sum썼었던거

```python
tips_10['total_bill'].iloc[:10].mean()
```

```python
tips_10_median = tips_10['total_bill'].median()
tips_10_median
```



R

- 파이썬은 0부터 시작, R은 1부터 시작

- Start:end -> R은 end를 포함한다

- 슬라이싱 -> 판다스는 행에대한 선택, R은 열에 대한 선택(행 슬라이싱하려면 , 를 더 붙여주어야함)

- 통계학자들이 만듦 (멀티환경에 익숙하지 않음 단일로 동작, 빅데이터 환경에 적합하지 않음 그래서 파이썬 자바가 강세임)

- 데이터 타입 종류 : **벡터**(모든타입의 기본), 메트릭스, 어레이, **데이터 프레임**, 리스트 등

  파이썬 : 리스트, 튜플, 딕셔너리

- Dplyr / gglot
- 판다스의 shape과 같은 개념 = dim
- Dplyr  의 여러 함수들 (열선택 : select / 변수생성 : mutate / 변수명 변경 : rename)
- Geom_point : 산점도 
- 바차드(bar) / col() 의 차이
- 벡터를 생성하는 함수 : c() / sequence / rap 등 
- 파이프 연산자 %>%
- 몫 연산자 %/% , 나머지 연산자 %%
- aes(x, y)
- Xlim. ylim
- xscale
- ggplot 기반으로 시계열 그래프 그리기, 맵그리기, 인터랙티브 그래프 그리는것



```R
# 1단계.평균표 만들기
df_mpg <- mpg %>%
  group_by(drv) %>%
  summarise(mean_hwy = mean(hwy))
```

