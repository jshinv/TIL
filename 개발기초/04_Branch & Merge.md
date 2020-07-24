# Branch & Merge



### 1. Branch

### 1.1 생성하기

```shell
// 브랜치 생성하기
$ git branch [브랜치명]
```



### 1. 2 위치 확인하기

``` shell
// 현 브랜치 위치 확인하기
$ git branch
```



### 1.3 이동하기 / switch

```shell
// 브랜치 이동하기
$ git switch [이동할 브랜치명]
```



### 1.4 새로 생성하고 그 branch로 이동하기

```shell
// 브랜치 새로 생성하고 그 브랜치로 이동
$ git switch -c new
```



### 1.5 로그 한줄로 보기

```shell
// 로그 한줄로 보기
$ git log --oneline
```

```shell
// head가 가르치는것이 내가 있는 브랜치(공간)
// 브랜치를 변경하면 로컬에서 보여지는 파일도 변경되어 보여진다
$ git log --oneline
(HEAD -> master, new)
```



### 1.6 삭제하기

```shell
// 브랜치 삭제하기
$ git branch -d [지울 브랜치명]
```



---



### 2. Merge

### 2.1 병합하기

```shell
// 브런치 합치기
$ git merge [병합을할 브랜치 이름 - 병합은 마스터에서]

// 이상한 화면으로 들어간다, 
// $:wp -> 저장하고 끝내는것(write & quit)
> esc + esc + esc $:wq

// 합쳐진 플로우를 그래프로 확인이 가능하다
$ git log --oneline --graph
```



### 2.2 이전 브랜치로 돌아가기

```shell
$ git checkout
```



---



### Merge Scenario

[visualizing](https://git-school.github.io/visualizing-git/)

#### 1. Fast Forward Merge

브랜치 분기가 일어났지만, merge 시점에서 branch 한쪽에서만 commit 들이 쌓여 있는경우

(ex. new 에만 commit 이 있고, master 에는 없던 경우)



#### 2. Auto -Merge

merge 시점에 양쪽 브랜치에 commit들이 쌓여 있지만,  Conflict 가 발생하지 않는 경우



#### 3. Merge-Conflict 발생

merge 시점에 양쪽 브랜치에 commit들이 쌓여 있고, Conflict 가 발생하는 경우

- 동일 파일내에 상충하는 내용이 있을 경우



---



### Ect. 참고

```shell
// ??
$ git merge new -no--ff
```



### Error

```shell
// Merge중 에러
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

> shell에서 위의 에러가 난뒤, 코드를 확인해 보면 아래와 같이 보이게 된다.
>
> 아래의 내용중 필요한 부분만 저장한뒤 다시 commit

```html
<<<<<<< HEAD
이건 master 브랜치에서 작업한것 (master)
=======
이건 New  브랜치에서 작업한것 (new)
>>>>>>> new
```