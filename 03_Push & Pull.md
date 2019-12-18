

# Push & Pull



### 1. git 생성하기

```shell
// git 생성
$ git init
```



### 2. git에 올라간 파일 복제하기

```shell
$ git clone [주소이름]
```



### 3. git에서 관리하는 폴더에서 신규파일 생성하기

```shell
// 파일추가
$ git add [파일명]

// 파일의 상태를 확인한다
$ git status
```



### 4. git에 파일 푸시하기

```shell
$ git add [추가된 파일]
// 다중파일추가

$ git add [추가할 파일1][추가할 파일1]
// 현재폴더의 모든거 다 추가

$ git add .

$ git commit -m "메시지를 넣는다"
$ git log

// git 에 처음 올릴때만 remote 작성
$ git remote add origin [원격저장소 주소: https://github.com/jshinv/TIL.git]
$ git remote -v
$ git push origin master
```



### 5.  git에 올라간 파일 삭제하기

######  5.1. 원격저장소 파일 삭제하기

```shell
// 1.원격 저장소와 로컬 저장소에 있는 파일 or 디렉토리 삭제
$ git rm [파일명]
$ git rm -r [디렉토리명]
$ git rm -f [강제삭제]

// 2.원격저장소에 있는 파일삭제, 로컬저장소 파일은 삭제 하지 않는다
$ git rm --cached [파일명]

// 만약, 폴더 하위의 모든을 삭제 하고 싶다면?
$ git rm --cached -r [폴더명]
```

###### 5.2. 원격 저장소에 적용하기

```shell
// 수정할 내용을 커밋
$ git commit -m "수정할 내용을 입력하세요"

// 원격저장소(origin)에 push
$ git push origin master
```



### Ect. 참고

```shell
// 파일을 셀에서 확인한다
$ cat [파일명]

// 로그 한줄로 보기
$ git log --oneline
```



### Error

```shell
// 리스트로 들어갔을때
$ q

// 먼가 나올수 없는 화면일때
esc버튼 esc버튼 esc버튼 + $ :q
```
