### Thymeleaf

> 아래의 표현방식을 권장한다.(html에서 이렇게 쓸것)

```html
아이디
<span th:text="${user.userId}"></span>
<br> 이름:
<span th:text="${user.userName}"></span>
<br> 나이:
<span th:text="${user.userAge}"></span>
```



---

### Pagination

http://localhost:8080/linkUrl?now_page=3

> 주소 + ? + 변수값



###### Controller

```java
@Controller
public class ThymeleafController {
	@GetMapping("/linkUrl")
	public String linkUrl(
//			파라미터로 Start와 End 값을 받는다
//			@RequestParam int start,
//			@RequestParam int end,
			@RequestParam(defaultValue="1") int now_page,
//			모델을 컨트롤러 안에서 만든다
			Model model) {
//		모델을 만들어서 값을 변경한뒤 View에 보여준다
		int start = (now_page -1) / 10 * 10 +1;
		int end = start + 9;
		model.addAttribute("start", start);
		model.addAttribute("end", end);
		model.addAttribute("now_page", now_page);
		return "linkUrl";
	}
}
```

###### Thymleaf

```html
<th:block th:each="page : ${#numbers.sequence(start, end)}">
	<span th:if="${now_page == page}" th:text="${page}"></span>
	<a href="javascript:;" th:unless="${now_page == page}">[[${page}]]</a>
</th:block>
```



---



