# Docker



### Mac

1. 우분투 설치하기

   ```shell
   $ docker pull ubuntu:14.04
   ```

   

2. 우분투 실행하기

   ```shell
   $ docker run -it ubuntu
   ```

   

3. 빠져나오기

   ```shell
   $ exit
   ```



4. 이미지 삭제하기

   ```shell
   $ docker rmi [OPTIONS] IMAGE [IMAGE...]
   ```

   

---



##### Docker 명령어

| **버전 확인**              | $ docker -v                                             |
| -------------------------- | ------------------------------------------------------- |
| **이미지 다운로드**        | $ docker pull [이미지 명]                               |
| **다운로드된 이미지 목록** | $ docker images                                         |
| **컨테이너 생성**          | $ docker create [옵션] [이미지 명]                      |
| **컨테이너 생성 및 실행**  | $ docker run [옵션] [이미지 명]                         |
| **컨테이너 실행**          | $ docker start [컨테이너 명]                            |
| **컨테이너 재실행**        | $ docker restart [컨테이너 명]                          |
| **컨테이너 접속**          | $ docker attach [컨테이너 명]                           |
| **컨테이너 정지**          | $ docker stop [컨테이너 명]                             |
| **실행중인 컨테이너 목록** | $ docker ps                                             |
| **정지된 컨테이너 목록**   | $ docker ps -a                                          |
| **컨테이너 명 변경**       | $ docker rename [기존 컨테이너 명] [새로운 컨테이너 명] |
| **컨테이너 삭제**          | $ docker rm [컨테이너 명]                               |