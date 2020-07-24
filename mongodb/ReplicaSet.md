# ReplicaSet & Sharding



### ReplicaSet

- 권장 : 3개 이상

- 데이터 복제

- Primary 에서 작업한 내용을 Sencondary 에 복제해 데이터를 보관하는 개념
- Localhost 를 Add 해주면 Secondary 폴더 생성이 가능하다.
- 데이터 입력 및 수정은 Primary에서 작업한다.

- Secondary 사용시에는 localhost서버를 구동시켜야 데이터가 복제될 수 있다. 



---

### Secondary 서버 추가 / 삭제 / 확인 - 명령어

1. 새로운 Secondary 서버 실행
   (ex. mongod –port 20003 …)
2. Primary 서버 접속 후
   rs.add('localhost:20003')
3. ReplicaSet 상태 확인
   rs.conf() 4. rs.remove('localhost:20003') 



### Sharding

- 권장 : 3개 이상

- 응용 + 중계 + 개체

- Mongos & Config = 중계개체
  - config : Sharding을 위한 메타 데이터를 저장 (데이터의 위치 정보 저장)
  - mongos : Client의 요청 처리, config 서버의 메타 데이터를 이용하여 각 MongoDB의 데이터에 접근
  - mongod : MongoDB의 데이터 서버 (상황에 따라 레플리카셋으로 구성)

