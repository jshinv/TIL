# naver

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Naver 파파고 번역</title>
</head>
<body>
	<input type="text" id="text">
	<button>번역하기</button>
	<hr>
	
	<!-- 자바스크립트(jQuery) AJAX 활용  -->
	<script src ="http://code.jquery.com/jquery-3.1.1.min.js"></script>
	<script>
	 $('button').click(function(){ // 버튼을 클릭하면 ...
		 $.ajax({
			 url : '/getNaver',
			 type : 'get',
			 data : {'text': $('#text').val() },
			 success : function(res){
				 /* console.log(res); */
				 var message = res.message;
				 var result = message.result;
				 var translatedText = result.translatedText;
				 var html = '<h1>' + translatedText + '</h1>';
				 $('hr').after(html);
			 }
		 })
	 });
	
	</script>
</body>
</html>
```



[http://ggoreb.com/m/spring_boot/%EC%8A%A4%ED%94%84%EB%A7%81%EB%B6%80%ED%8A%B8-1.pdf](http://ggoreb.com/m/spring_boot/스프링부트-1.pdf)

Thyme leaf : 49P



[http://ggoreb.com/m/spring_boot/%EC%8A%A4%ED%94%84%EB%A7%81%EB%B6%80%ED%8A%B8-2.pdf](http://ggoreb.com/m/spring_boot/스프링부트-2.pdf)

48 P