---

---



# SpringBoot



1. STS 설치
2. Lombok 설치 (STS위치에 설치, 메소드 자동생성)
3. Controller Class생성
   - 메소트(GetMapping / @RequestMapping)
   - ResponseBody(JSON) 또는 RestController(HTML)



---



###### lombok.jar install (window)

> Mac 은 그냥 다운로드하면 사용가능

```shell
$ java -jar lombok.jar
```



### 단축키

Commanc + Shift + F : 텍스트 정렬

Commanc + Shift + O : Import등 환경 맞추기



### Log for error

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

**Model** : Repository(서비스 로직을 통하여 반환되어 브라우저에 표시될 정보)

**View** :  template, 자바스크립트 처리(단순뷰)

- 클라이언트는 3가지로 응답받을수 있다.
  1. 화면
  2. 이미지 파일
  3. 파일 다운로드

**Controller** : controller(중요한 연산)

**Service** : 중간에서 요청과 응답을 처리(핸들러)

---



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
  
  // String : 경로/파일명
  // html 파일아래 string 파일을 찾아라
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

- POST : 데이터 저장 (주소창에 POST 입력하면 화면 접근이 불가능하다)
  - TEST : 구글확장 프로그램에서 `Talend API Tester - Free Edition` 설치

- GET :  데이터 가져오기 ( 브라우져에서 접근하는 방식은 무조건 GET방식 사용)
- PUT :  데이터 수정
- DELETE : 데이터 삭제



> ## GET과 POST의 차이
>
> GET은 Idempotent, POST는 Non-idempotent하게 설계되었습니다.
> Idempotent(멱등)은 수학적 개념으로 다음과 같이 나타낼 수 있습니다.
>
> > 수학이나 전산학에서 연산의 한 성질을 나타내는 것으로, 연산을 여러 번 적용하더라도 결과가 달라지지 않는 성질
>
> 즉, 멱등이라는 것은 **동일한 연산을 여러 번 수행하더라도 동일한 결과**가 나타나야 합니다.
> 여기서 GET이 Idempotent하도록 설계되었다는 것은 GET으로 **서버에게 동일한 요청을 여러 번 전송하더라도 동일한 응답이 돌아와야 한다는 것**을 의미합니다. 이에 따라 GET은 설계원칙에 따라 서버의 데이터나 상태를 변경시키지 않아야 Idempotent하기 때문에 **주로 조회를 할 때에 사용**해야합니다. 예를 들어, 브라우저에서 웹페이지를 열어보거나 게시글을 읽는 등 조회를 하는 행위는 GET으로 요청하게 됩니다.
>
> 반대로 POST는 Non-idempotent하기 때문에 **서버에게 동일한 요청을 여러 번 전송해도 응답은 항상 다를 수 있습니다**. 이에 따라 POST는 서버의 상태나 데이터를 변경시킬 때 사용됩니다. 게시글을 쓰면 서버에 게시글이 저장이 되고, 게시글을 삭제하면 해당 데이터가 없어지는 등 POST로 요청을 하게 되면 서버의 무언가는 변경되도록 사용됩니다. 이처럼 POST는 생성, 수정, 삭제에 사용할 수 있지만, 생성에는 POST, 수정은 PUT 또는 PATCH, 삭제는 DELETE가 더 용도에 맞는 메소드라고 할 수 있습니다.
>
> 마지막으로 웹페이지를 조회할 때, 링크를 통해 특정 페이지로 바로 이동하려면 해당 링크와 관련된 정보가 필요한데 POST는 요청 데이터가 Body에 담겨 있기 때문에 링크 정보를 가져올 수 없습니다. 반면, GET은 URL에 요청 파라미터를 가지고 있기 때문에 링크를 걸 때, URL에 파라미터를 사용해 더 디테일하게 페이지를 링크할 수 있습니다.
>
> GET과 POST는 이처럼 큰 차이가 있기 때문에 설계원칙에 따라 적절한 용도로 사용해야합니다.

참고 URL : https://hongsii.github.io/2017/08/02/what-is-the-difference-get-and-post/



---



### 요청처리

- **RequestParam** (편리함) : 컨트롤러 메소드의 인자명과 동일
  - 파라미터 명칭에 맞게 변수 사용
  - 파라미터 종류 및 개수 상관없이 사용
-  **ModelAttribute**(명확함) : 모델 클래스의 변수명과 동일
  - Model / DTO / VO 등 객체와 연계하여 활용
  - JPA, MyBatis 등 ORM 프레임워크 활용 



---



### LoginController

```java
package com.jshinv.basic.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class LoginCotroller {
	// 보여주는 페이지
  @GetMapping("/login")
	public String login() {
		return "login";
	}
	
  // 프로그램이 동작한 이후 보여지는 페이지
  // 위의 login과 이름은 같으나 주소를 통해 직접 접근은 불가능(Post방식)
	@PostMapping("/login")
	@ResponseBody
	public String loginPost(
			@RequestParam("id") String id,
			@RequestParam("pw") String pw) {
		
		String dbId = "boot";
		String dbPw = "1234";
		
		if(dbId.equals(id) && dbPw.equals(pw)) {
			return "로그인 성공";
		}
		
		return "로그인 실패";
	}
}

```



---



### Session & Cookie

**HTTP & HTTPS**

> HTTPS : Hyper Tet Transfer Protocol [Secure]
>
> 둘다, 상태를 기억할 수 없다 (Stateless)

> 서버에 접속하면, 티켓이 발행되고 클라이언트는 서버에 티켓을 가지고 통신한다
> (로컬 브라우저 =  쿠키 / 서버 = 세션)

**Cookie**

- 특징
  - 클라이언트(브라우저) 로컬에 저장되는 키와 값이 들어있는 작은 데이터 파일
  - 사용자 인증이 유효한 시간을 명시할 수 있으며, 유효 시간이 정해지면 브라우저가 종료되어도 인증이 유지
  - 쿠키는 클라이언트의 상태 정보를 로컬에 저장했다가 참조
- 사용 예 
  - 방문 사이트에서 로그인 시, "아이디와 비밀번호를 저장하시겠습니까?"
  - 쇼핑몰의 장바구니 기능
  - 자동로그인, 팝업에서 "오늘 더 이상 이 창을 보지 않음" 체크, 쇼핑몰의 장바구니

**Session**

- 특징
  - 각 클라이언트에게 고유 ID 부여
  - 세션 ID로 클라이언트를 구분하여 클라이언트 요구에 맞는 서비스 제공
  - 보안면에서 쿠키보다 우수
  - 사용자 많을수록 서버 메모리를 많이 차지하게됨
- 사용예
  - 로그인 같이 보안상 중요한 작업

출처: https://interconnection.tistory.com/74 [라이언 서버]

