# Kakao Map

### EX - 위도/경도 변환

###### RestTemplateController.java

```java
package com.jshinv.basic.controller;

import java.io.UnsupportedEncodingException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.URLEncoder;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.http.RequestEntity;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@RestController
public class RestTemplateController {
	@GetMapping("/getKakao")
	public ResponseEntity<Map> getKakao(
			@RequestParam("address") String address) {
		RestTemplate rt = new RestTemplate();
		RequestEntity requestEntity = null;
		try {
			requestEntity = RequestEntity
					.get(new URI("https://dapi.kakao.com/v2/local/search/address.json?query="
							+ URLEncoder.encode(address, "utf-8")))
					.header("Authorization", "KakaoAK d4be7b479f4b4cbd99bd19ae87f88b4b").build();
		} catch (UnsupportedEncodingException e) {
			e.printStackTrace();
		} catch (URISyntaxException e) {
			e.printStackTrace();
		}
		ResponseEntity<Map> entity = rt.exchange(requestEntity, Map.class);
		return entity;
	}

}
```

###### Kakao.html

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Kakao 위도/경도 변환</title>
</head>
<body>
	<input type="text" id="address">
	<button>위도/경도 변환</button>
	<hr>
	<!-- 자바스크립트(jQuery) AJAX 활용  -->
	<script src ="http://code.jquery.com/jquery-3.1.1.min.js"><</script>
	<!-- getkakao 주소를 호출  -->
	<!-- parsing 후 화면에 출력  -->
	<script>
	 $('button').click(function(){ // 버튼을 클릭하면 ...
		 $.ajax({
			 url : '/getKakao',
			 type : 'get',
			 data : {'address': $('#address').val() },
			 success : function(res){
				 console.log(res);
			 }
		 })
	 });
	
	</script>
</body>
</html>
```

###### ServiceController.java

```java
package com.jshinv.basic.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class ServiceController {
	@GetMapping("/kakao")
	public String kakao() {
		 return "kakao";
	}
}
```

