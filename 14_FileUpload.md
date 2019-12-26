# FileUpload

### form type

> form 태그에 무조건 들러가야 하는것
>
> > `enctype="multipart/form-data"`
> >
> > `method = post` , `name="file"`

```html
<form method="post" enctype="multipart/form-data">
  // multiple : 다중파일 업로드가 가능하다
	<input type="file" name="file" multiple><br>
	<input type="submit" value="업로드">
</form>
```



### EX

###### controller/UploadController.java (MultipartHttpServletRequest)

```java
package com.jshinv.basic.controller;

import java.io.File;
import java.io.IOException;
import java.util.List;

import org.apache.tomcat.jni.FileInfo;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;

@Controller
public class UploadController {
	@GetMapping("/upload1")
	public String upload1() {
		return "upload1";
	}

	@PostMapping("/upload1")
	@ResponseBody
	public String upload1Post(MultipartHttpServletRequest mRequest) {
		String result = "";
		
		List<MultipartFile> mFiles =
				mRequest.getFiles("file");
		
		for(int i = 0; i < mFiles.size(); i++) {
			
			// mFile = 업로드된 파일정보
			MultipartFile mFile = mFiles.get(i);
			
			String oName = mFile.getOriginalFilename();
			result += oName + "\n";
			
			// 지정경로에 지정 파일명으로 저장
			try {
				mFile.transferTo(new File("/Users/jshin/work/jshinv/spring/img/" + oName));
			} catch (IllegalStateException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
		return result;
	}

	@GetMapping("/upload2")
	public String upload2() {
		return "upload2";
	}

	@PostMapping("/upload2")
	@ResponseBody
	public String upload2Post(@RequestParam("file") MultipartFile mFile) {
		String result = "";
		String oName = mFile.getOriginalFilename();
		result += oName + "\n";
		return result;
	}

	@GetMapping("/upload3")
	public String upload3() {
		return "upload3";
	}

	@PostMapping("/upload3")
	@ResponseBody
	public String upload3Post(@ModelAttribute FileInfo info) {
		String result = "";
		String oName = info.getFile().getOriginalFilename();
		result += oName + "\n";
		return result;
	}
}
```

###### templates/upload1.html

```html
<form method="post" enctype="multipart/form-data">
 <input type="file" name="file" multiple><br>
 <input type="submit" value="업로드">
</form>
```

###### application.properties

```java
…
# file upload
spring.servlet.multipart.max-file-size=2097152
spring.servlet.multipart.max-request-size=2097152
```



참고 URL(by baeldung) : https://www.baeldung.com/spring-file-upload



---



# Download

### content -type : mime types

 참고 URL : https://www.freeformatter.com/mime-types-list.html



### EX

###### controller/DownloadController.java

```java
package com.jshinv.basic.controller;

import java.io.File;
import java.io.FileInputStream;
import java.net.URLEncoder;

import org.springframework.core.io.InputStreamResource;
import org.springframework.core.io.Resource;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;


@Controller
public class DownloadController {
	@GetMapping("/download")
	public ResponseEntity<Resource> download() throws Exception {
		File file = new File("/Users/jshin/work/jshinv/spring/img/sample.jpg");
		InputStreamResource resource = new InputStreamResource(new FileInputStream(file));
		return ResponseEntity.ok()
				.header("content-disposition", "filename=" + URLEncoder.encode(file.getName(), "utf-8"))
				//application/octet-stream : 바로 다운로드 
//				.contentLength(file.length()).contentType(MediaType.parseMediaType("application/octet-stream"))
				
				// MediaType.parseMediaType("image/jpeg") : 화면에 이미지 바로 출력 
				.contentLength(file.length()).contentType(MediaType.parseMediaType("image/jpeg"))
				.body(resource);
	}
}
```

