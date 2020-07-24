# Signin, Signout

### Ex

###### UserController

```java
package com.example.board.controller;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import com.example.board.model.User;
import com.example.board.repository.UserRepository;

@Controller
public class UserController {
	@Autowired
	UserRepository userRepository;

	@Autowired
	HttpSession session;
	
	@GetMapping("/signup")
	public String signup() {
		return "signup";
	}

	@PostMapping("/signup")
	public String signupPost(@ModelAttribute User user) {
		userRepository.save(user);
		return "redirect:/";
	}

	@GetMapping("/signin")
	public String signin() {
		return "signin";
	}

	@PostMapping("/signin")
	public String signinPost(@ModelAttribute User user) {
		User dbUser = userRepository.findByEmailAndPwd(user.getEmail(), user.getPwd());
		if (dbUser != null) {
			session.setAttribute("user_info", dbUser);
		}
		return "redirect:/";
	}

	@GetMapping("/signout")
	public String signout() {
		session.invalidate();
		return "redirect:/";
	}

}
```

###### UserRepository

```java
package com.example.board.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.board.model.User;

public interface UserRepository extends JpaRepository<User, Long> {
	User findByEmailAndPwd(String email, String pwd);
}
```



###### Signin.html

```html
<!DOCTYPE html>
<html lang="utf-8">

<head th:replace="common/head">
</head>
<body>
	<nav class="navbar navbar-inverse" th:replace="common/nav"></nav>
	<div class="jumbotron">
		<div class="container text-center">
			<div class="row">
				<div class="col-md-6 col-md-offset-3">
					<form method="post" action="/signin">
						<div class="form-group">
							<label for="email">Email:</label> <input type="text"
								class="form-control" id="email" name="email">
						</div>
						<div class="form-group">
							<label for="pwd">Password:</label> <input type="password"
								class="form-control" id="pwd" name="pwd">
						</div>
						<button class="btn btn-primary btn-block" id="signin">Sign in</button>
						<button class="btn btn-danger btn-block" id="signup">Sign up</button>
					</form>
				</div>
			</div>
		</div>
	</div>

	<footer class="container-fluid text-center" th:replace="common/footer">
	</footer>
	<script>
		$("#signin").click(function() {
			$("form").submit();
			return false;
		});
		$("#signup").click(function() {
			location = "/signup";
			return false;
		});
	</script>
</body>
</html>
```



참고 URL 

> 부트스트랩
>
> https://getbootstrap.com/docs/3.4/css/
>
> https://www.w3schools.com/bootstrap/bootstrap_buttons.asp

