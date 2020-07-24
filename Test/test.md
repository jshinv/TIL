

### Java

```java
publick class Test{
  
}
```





필기 60

수행평가 60 (Java / html,css, javascript / springboot(resttemplate))

- Java Scanner를 이용한 입력

  ```java
  package test;
  import java.util.Scanner;
  
  // main 입력후 Ctrl + Space
  public class Test {
  	public static void main(String[] args) {
  		// syso 입력후 Ctrl + Space
      System.out.println("입력해 주세요");
      Scanner s = new Scanner(System.in);
  		// 입력메소드, String은 하나만 쓰자 next로 사용
      int price = s.nextInt(); // 숫자 입력
      String title = s.next(); // 문자열 입력(줄바꿈 문자인 \n 포함)
      String category = s.nextLine(); // 문자열 입력(줄바꿈 문자인 \n 생략)
  		
      // 클래스를 쓸때 꼭 new 를 써야함 
      상품 p = new 상품();
      p.price = price;
      p.title = title; 
      p.category = category;
      System.out.println(p);
      
      // int a = s.nextInt();
  		// int b = s.nextInt();
  		// int r = a + b;
  		// System.out.println(r);
  	}
  }
  
  // 클래스로 저장(담아주기)
  class 상품{
    int price; 
    String title;
    String category;
    
    @Override
    public String toString() {
  	  return "price : " + price;
    }
    
  }
  ```

  

- 입력된 자료를 클래스로 저장

---

### HTML / JS / JS / jQuery

- 자바 요구조건과 동일
- 입력 UI만들기 

---

### Spring boot

RestTemplate

JSON Parsing