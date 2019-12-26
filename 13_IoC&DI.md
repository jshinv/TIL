# IoC & DI

### IoC & DI

> **IoC**(Inversion of Control)
> **DI**(Dependency Injection)

```java
// Autowired = 다른 class에서 만든것을 선언한 페이지에서 사용할 수 있게 해준다
@Autowired
ProductRepository productRepository;
// ProductRepository 를 불러라, 거기에서 사용한 함수등을 productRepository 에서도 사용할 수 있게 해라
// productRepository 는 변수명으로 내 마음대로 사용할수 있다.
```



```java
@Controller
@Service
@Repository
@Componenet
```

