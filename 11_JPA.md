# JPA

### JAP

>  Java Persistence API

- 인터페이스 모음
- 특정 DataBase에 종속되지 않고 자동으로 변환시켜 준다



---

### 주요 메소드

| 의미                               | Code                     |
| ---------------------------------- | ------------------------ |
| 데이터 입력 및 수정(insert/update) | save(T t)                |
| 데이터 조회(select)                | findAll() / findById(ID) |
| 데이터 삭제(delete)                | delete(T t)              |
| 데이터 개수 확인                   | count()                  |



### 사용자 정의 메소드 규칙

| 키워드             | 메소드명                                                     | 키워드       | 메소드명                       |
| ------------------ | ------------------------------------------------------------ | ------------ | ------------------------------ |
| And                | **findBy**Lastname**And**Firstname                           | Like         | findByFirstnameLike            |
| Or                 | **findBy**Lastname**Or**Firstname                            | NotLike      | findByFirstnameNotLike         |
| Is, Equals         | **findBy**Firstname, findByFirstnameIs, findByFirstnameEquals | StartingWith | findByFirstnameStartingWith    |
| Between            | **findBy**StartDate**Between**                               | EndingWith   | findByFirstnameEndingWith      |
| LessThan           | **findBy**Age**LessThan**                                    | Containing   | findByFirstnameContaining      |
| LessThan Equal     | findByAgeLessThanEqual                                       | OrderBy      | findByAgeOrderByLastNameDesc   |
| GreaterThan        | findByAgeGreaterThan                                         | Not          | findByLastnameNot              |
| GreaterThan Equal  | findByAgeGreaterThanEqual                                    | In           | findByAgeIn(Collection ages)   |
| After              | findByStartDateAfter                                         | NotIn        | findByAgeNotIn(Collection age) |
| Before             | findByStartDateBefore                                        | True         | findByActiveTrue()             |
| IsNull             | findByAgeIsNull                                              | False        | findByActiveFalse()            |
| IsNotNull, NotNull | findByAge(Is)NotNull Ig                                      | IgnoreCase   | findByFirstnameIgnoreCase      |



---

### EX

######  application.properties

```java
logging.level.com.jshinv.basic=trace

# datasource
spring.datasource.url=jdbc:h2:~/test
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=

# jpa
spring.jpa.hibernate.ddl-auto=update
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.jpa.show-sql=true
```

###### model/Product.java

```java
package com.ggoreb.basic.model;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import lombok.Data;
@Data
@Entity
public class Product {
@Id
@GeneratedValue(strategy = GenerationType.AUTO)
private long id;
private String name;
private int price;
private int count;
}
```

######  repository/ProductRepository.java

```java
package com.ggoreb.basic.repository;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import com.ggoreb.basic.model.Product;
@Repository
public interface ProductRepository extends JpaRepository<Product, Long>{
}
```

###### controller/JpaController.java

```java
package com.ggoreb.basic.controller;
import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;
import com.ggoreb.basic.model.Product;
import com.ggoreb.basic.repository.ProductRepository;

@RestController
public class JpaController {
@Autowired
ProductRepository productRepository;
@GetMapping("/jpa/product")
public List<Product> product() {
  List<Product> list = productRepository.findAll();
  return list;
  }
  @PostMapping("/jpa/product")
  public String productPost(@ModelAttribute Product product) {
  productRepository.save(product);
  return "redirect:/jpa/product";
  }
}
```



---

