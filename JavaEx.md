# JavaEx



### 반복문

###### 구구단

```java
package ch04;

public class Gugudan1 {
	public static void main(String[] args) {
		for (int i = 1; i <= 9; i++) {
			for (int j = 2; j <= 9; j++) {
				System.out.print(j + " * " + i + " = " + (i * j) + "\t");
			}
			System.out.println();
		}
	}
}
```



###### 별만들기

```java
package ch04;

public class Star1 {
	public static void main(String[] args) {
		for (int a = 1; a <= 5; a++) {
			for (int b = 1; b <= a; b++) {
				System.out.print("*" + " ");
			}
			System.out.println();
		}
	}
}
```



### 조건문

###### 과일등급

```java
package ch06;

//수박의 무게가 10kgkg이 넘으면 1등급, 7kgkg이 넘으면 2등급, 4kgkg이 넘으면 3등급,
//나머지는 4kg등급을 부여하는 checkGrade 메소드 만들기
public class Exam6_1_1 {

	int checkGrade(int w) {
		int grade = 0;
		if (w > 9) {
			grade = 1;
		} else if (w > 6 ) {
			grade = 2;
		} else if (w > 3) {
			grade = 3;
		} else {
			grade = 4;
		}
		
		return grade;
	}

	public static void main(String[] args) {
		Exam6_1_1 n = new Exam6_1_1();
		int grade = n.checkGrade(7);
		System.out.println(grade + " 등급입니다.");
	}
}
```



###### 가위바위보

```java
package ch04;

import java.util.Random;
import java.util.Scanner;

public class 가위바위보 {
	public static void main(String[] args) {
		System.out.println("입력해 주세요");
		Scanner s = new Scanner(System.in);
		int me = s.nextInt() ;
		
		Random r = new Random();
		
		int com = r.nextInt(3); // 0 ~ 2 숫자가 랜덤으로 들어감
		
		
		if((me + 1) % 3 == com) {
			System.out.println("상대방 이김");
		} else if(me == com) {
			System.out.println("비김");
		} else {
			System.out.println("내가 이김");
		}
	}
}

```



###### 카드번호 맞추기

```java
package ch04;

import java.util.Scanner;

public class CardApp {
	public static void main(String[] args) {
		int startNum = 0; // 최소 카드 번호
		int endNum = 0; // 최대 카드 번호
		

		Scanner scan = new Scanner(System.in);

		System.out.print("카드의 시작 번호를 입력해주세요. > ");
		startNum = scan.nextInt(); // 시작 번호 입력
		while (true) {
			System.out.print("카드의 마지막 번호를 입력해주세요. > ");
			endNum = scan.nextInt(); // 마지막 번호 입력
			if (endNum <= startNum) { // 마지막 번호가 시작 번호보다 크지 않다면
				System.out.println("시작 번호보다 큰 번호를 입력해주세요.");
			} else { // 마지막 번호가 시작 번호보다 크다면
				break; // 반복문 강제 종료
			}
		}
		int cardNum = 0; // 랜덤으로 추출할 카드 번호
		while (true) {
			cardNum = (int) (Math.random() * (endNum + 1));
			// 시작과 마지막 번호 범위내의 숫자인지 확인
			if (cardNum >= startNum && cardNum <= endNum)
				break;
		}
		System.out.println("카드 번호를 입력해주세요.");
		while (true) {
			int userNum = scan.nextInt();
			int count = 0; // 시도횟수
			if (userNum < startNum || userNum > endNum) {
				System.out.println("입력범위를 초과하였습니다. 다시입력해 주세요");
				System.out.printf("시작번호: " + startNum + "\t" + "종료번호: " + endNum);
			} else {
				count++;
				if (userNum == cardNum) {
					System.out.println("맞혔습니다.");
					System.out.println("시도횟수: " + count);
					break;
				} else if (userNum == 99999) {
					System.out.println("프로그램을 종료합니다.");
					break;
				} else {
					if (userNum > cardNum)
						System.out.println("입력된 숫자보다 카드번호가 적습니다.");
					else
						System.out.println("입력된 숫자보다 카드번호가 큽니다.");
					System.out.println("다시 입력해주세요.");
				}
			}

		}
		scan.close();
	}
}
```

