

# SpringBoot



###### lombok.jar install (window)

> Mac 은 그냥 다운로드하면 사용가능

```shell
$ java -jar lombok.jar
```



### 단축키

Commanc + Shift + F : 텍스트 정렬

Commanc + Shift + O : Import등 환경 맞추기



### Controlle.java

```java
@RequestMapping("/")
	public String home() {
		// 개발하는 단계에서 사용 : trace , debug
		logger.trace("trace!");
		logger.debug("debug!"); // 개발단계에서 확인용
		
		// 프로그램이 돌아갈때 필요한 정보
		logger.info("info!"); // 운용 상 필요한 정
		logger.warn("warn!"); // 메모리 문제 등 경고
		logger.error("error!"); // 치명적인 오류
		
		return "home";
	}
```



### Log설정

###### application.properties

```
logging.level.com.jshinv.basic=trace
```

[Document](http://logback.qos.ch/manual/)



### 스프링 MVC

| 구성요소 설명     | 설명                                                         |
| ----------------- | ------------------------------------------------------------ |
| DispatcherServlet | 클라이언트의 요청을 컨트롤러에게 전달하고 컨트롤러가 리턴하는 결과를 View로 전달 |
| HandlerMapping    | 클라이언트의 요청을 어떤 컨트롤러가 처리할지 결정            |
| Controller        | 클라이언트의 요청대로 로직 수행 후 결과 리턴 (Model, View)   |
| ModelAndView      | 컨트롤러가 수행한 로직 결과 데이터(모델) 및 View 페이지에 대한 정보 를 담음 |
| ViewResolver      | ModelAndView에서 지정된 View 명을 기반으로 결과 처리 View 결정 |
| View              | 컨트롤러가 로직을 수행하고 ModelAndView에 저장된 결과를 화면으로 출력 (일반적으로 JSP 또는 Velocity 같은 뷰 템플릿 사용) |



### Controller_case

```java
package com.jshinv.basic.controller;

import java.util.HashMap;
import java.util.Map;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.servlet.ModelAndView;
import com.jshinv.basic.model.Member;

@Controller
public class HtmlController {
	@GetMapping("html/string")
	public String html() {
		return "html/string";
	}

	@GetMapping("html/void")
	public void htmlVoid() {
	}

	@GetMapping("html/map")
	public Map<String, Object> htmlMap(Map<String, Object> map) {
		Map<String, Object> map2 = new HashMap<String, Object>();
		return map2;
	}

	@GetMapping("html/model")
	public Model htmlModel(Model model) {
		return model;
	}

	@GetMapping("html/model_and_view")
	public ModelAndView htmlModel() {
		ModelAndView mav = new ModelAndView();
		mav.setViewName("html/model_and_view");
		return mav;
	}
	
  // 만들어져 있는 틀안에서 컨트롤러에서 넣어주는 데이터를 채워 넣음
  // 하나의 틀에 보여지는 컨텐트를 다르게 보여줄 수 있다.
	@GetMapping("html/object")
	public Member htmlObject() {
		Member member = new Member();
		member.setName("kim");
		return member;
	}
}
```



---



### 응답방식

- HTML : String
- JSON : map, array, list, object //  `@responseBody` 



---



### Http method

- POST : 데이터를 가져오기 (주소창에 POST 입력하면 화면 접근이 불가능하다)
  - TEST : 구글확장 프로그램에서 `Talend API Tester - Free Edition` 설치

- GET :  데이터 저장 ( 브라우져에서 접근하는 방식은 무조건 GET방식 사용)
- PUT :  데이터 수정
- DELETE : 데이터 삭제



