# Setting



### 아마존 웹서비스 EC2 

1. 계정등록(결제포함)

2. 콘솔 로그인

   https://console.aws.amazon.com/billing/home#/account

3. ect 접속

   - 리전을 서울로 설정(오른쪽 상단)

   - 인스턴스 시작 버튼 클릭

   - 아마존 리눅스 선택 (https://ap-northeast-2.console.aws.amazon.com/ec2/v2/home?region=ap-northeast-2#LaunchInstanceWizard:)

   - 프리티어 서비스에서 검토 및 시작 버튼 클릭

   - 시작하기 버튼클릭(기존 키페어 선택 또는 새키 페어 생성)

   - 키페어 저장(중요!!)

   - 인스턴스 시작

   - 인스턴스 목록에서 연결 버튼 클릭 **C2 인스턴스 연결(브라우저 기반 SSH 연결)**

   - ```shell
     $ sudo yum install python3
     ```

   - 인스턴스 상태 종료 : 인스턴스는 자정이후 삭제되며 복구되지 않는다(인스턴스 상태: terminated)



---



### 배포판 만들기

- 인스턴스 생성

- 선택 : Ubuntu Server 18.04 LTS (HVM), SSD Volume Type

- 기존 키페어 선택(사전에 키페어 생성을 한 경우)

  >엑세스 확인 체크박스 선택

- putty 또는 Xshell (https://www.netsarang.com/ko/xshell/) 다운로드

  > putty는 한글이 깨짐

