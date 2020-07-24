# jQuery선택자 모음

# [![HOME으로 가기](http://bamtol.net/v5/img/bamtol_logo.png)](http://bamtol.net/v5/)

![기본](http://bamtol.net/v5/img/ts01.gif) ![크게](http://bamtol.net/v5/img/ts02.gif) ![더크게](http://bamtol.net/v5/img/ts03.gif)

1. #### [Design](http://bamtol.net/v5/bbs/board.php?bo_table=pp_js&wr_id=18#)

2. #### [Programming](http://bamtol.net/v5/bbs/board.php?bo_table=pp_js&wr_id=18#)

3. #### [Community](http://bamtol.net/v5/bbs/board.php?bo_table=pp_js&wr_id=18#)

## Javascript

# 제이쿼리 | 제이쿼리 - 선택자, 이벤트핸들러, 속성, 메소드 모음



- [이전글](http://bamtol.net/v5/bbs/board.php?bo_table=pp_js&wr_id=19)
- [다음글](http://bamtol.net/v5/bbs/board.php?bo_table=pp_js&wr_id=16)

- [목록](http://bamtol.net/v5/bbs/board.php?bo_table=pp_js&page=)

## 

**---------------- 프레임워크 선언 -----------------**

<//script src="http://code.jquery.com/jquery-latest.js"></script//>
<//script type="text/javascript" src="http://code.jquery.com/jquery-1.6.2.min.js"></script//>

<!-- 2015.05.15 -->

<script src="//code.jquery.com/jquery-1.11.3.min.js"></script>

<script src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>    ---------------- 속성, 메소드 활용방법 ------------  속성 : $("선택자").attr("속성명","속성값");  메소드 : $("선택자").click( function(){ 액션1; 액션2; ... } );   ------- 선택자 표기----------------  $("*") $("태그명") $(".클래스명") $("태그명.클래스명") $("#ID명") $("#ID명 종속태그명") = $("#ID명").find("종속태그명") $("#ID명, .클래스명, 태그명")    ---- DOM Selector ------------  $("선택자1 선택자2")  선택자1의 자손이면서 선택자2와 일치하는 모든 엘리먼트에 적용  $("선택자1 > 선택자2") 선택자1의 바로 아래 자손이면서 선택자2와 일치하는 엘리먼트에 적용  $("선택자1 + 선택자2")  선택자1의 형제 엘리먼트로 바로 다음에 나오는 엘리먼트 선택자2와 일치하는 엘리먼트에 적용  $("선택자1 ~ 선택자2") 선택자1의 형제 엘리먼트중에 선택자2와 일치하는 다음에 나오는 모든 엘리먼트에 적용  $("선택자1:has("선택자2")") 선택자2인 자손을 1개이상 가진 선택자1인 모든 엘리먼트에 적용  $("선택자:first") 선택자과 일치하는 것중 페이지에서 처음으로 일치하는 엘리먼트  $("선택자:last") 선택자과 일치하는 것중 페이지에서 마지막으로 일치하는 엘리먼트  $("선택자:first-child") 선택자과 일치하는 것중 첫번째 자식 엘리먼트  $("선택자:last-child") 선택자과 일치하는 것중 마지막 자식 엘리먼트  $("선택자:only-child") 선택자과 일치하는 것중 형제가 없는 모든 엘리먼트  $("선택자:nth-child(n)") //1~10 선택자과 일치하는 것중 n번째 자식 엘리먼트  $("선택자:nth-child(even | odd)") 선택자과 일치하는 것중 짝수 또는 홀수 자식 엘리먼트  $("선택자:nth-child(Xn+Y)")  전달된 공식에 따른 n번째 자식 엘리먼트, Y는 0인 경우 생략  $("선택자:even/odd") 페이지 전체의 짝수/홀수 번째 엘리먼트  $("선택자:eq(n)") // 0~9 n번째로 일치하는 엘리먼트  $("선택자:gt(n)") n번째로 엘리먼트(포함되지 않음) 이후의 엘리먼트  $("선택자:lt(n)") n번째로 엘리먼트(포함되지 않음) 이전의 엘리먼트  $(this).parent().next() 현재객체의 부모로부터 다음번째 엘리먼트...  $(this).parent().prev() 현재 객체의 부모로부터 이전번째 엘리먼트..

$(this).****children()
현재객체의 자식노드

$(this).children().each(function(index, elem){

//현재객체의 자식노드들이 각각 실행하는 함수, 마치 for( value in key){ ...} 와 비슷.

console.log(index +":"+elem.tagName);

}


**< 선택한 요소의 필터링 정리 >**

| 선택자            | 예제                      | 설명                                                         |
| :---------------- | :------------------------ | :----------------------------------------------------------- |
| :eq(n)            | `$("ul li:eq(3)")`        | 선택한 요소 중에서 인덱스가 n인 요소를 선택함.               |
| :gt(n)            | `$("ul li:gt(3)")`        | 선택한 요소 중에서 인덱스가 n보다 큰 요소를 모두 선택함.     |
| :lt(n)            | `$("ul li:lt(3)")`        | 선택한 요소 중에서 인덱스가 n보다 작은 요소를 모두 선택함.   |
| :even             | `$("tr:even")`            | 선택한 요소 중에서 인덱스가 짝수인 요소를 모두 선택함.       |
| :odd              | `$("tr:odd")`             | 선택한 요소 중에서 인덱스가 홀수인 요소를 모두 선택함.       |
| :first            | `$("p:first")`            | 선택한 요소 중에서 첫 번째 요소를 선택함.                    |
| :last             | `$("p:last")`             | 선택한 요소 중에서 마지막 요소를 선택함.                     |
| :animated         | `$(":animated")`          | 선택한 요소 중에서 애니메이션 효과가 실행 중인 요소를 모두 선택함. |
| :header           | `$(":header")`            | 선택한 요소 중에서 ``부터 ``까지의 요소를 모두 선택함.       |
| :lang(언어)       | `$("p:lang(ko)")`         | 선택한 요소 중에서 지정한 언어의 요소를 모두 선택함.         |
| :not(선택자)      | `$("input:not(:empty)")`  | 선택한 요소 중에서 지정한 선택자와 일치하지 않는 요소를 모두 선택함. |
| :root             | `$(":root")`              | 선택한 요소 중에서 최상위 루트 요소를 선택함.                |
| target            | `$("a[target='_blank']")` | 선택한 요소 중에서 웹 페이지 URI의 fragment 식별자와 일치하는 요소를 모두 선택함. |
| :contains(텍스트) | `$(":contains('Hello')")` | 선택한 요소 중에서 지정한 텍스트를 포함하는 요소를 모두 선택함. |
| :has(선택자)      | `$("p:has(span)")`        | 선택한 요소 중에서 지정한 선택자와 일치하는 자손 요소를 갖는 요소를 모두 선택함. |
| :empty            | `$(":empty")`             | 선택한 요소 중에서 자식 요소를 가지고 있지 않은 요소를 모두 선택함. |
| :parent           | `$(":parent")`            | 선택한 요소 중에서 자식 요소를 가지고 있는 요소를 모두 선택함. |



**------------- 속성 조건을 이용한 선택자 활용 ------**

$(Selector[attr])
attr 속성(attribute)값을 가지는 Selector 요소와 일치

$(Selector[attr = ”value”])
attr 속성의 값이 value와 동일한 값인 Selector 요소와 일치

$(Selector[attr != ”value”])
attr 속성의 값이 value와 같지 않은 값인 Selector 요소와 일치

$(Selector[attr ^= ”value”])
attr 속성의 값이 value 값으로 시작하는 Selector 요소와 일치

$(Selector[attr$=”value”])
attr 속성의 값이 value 값으로 끝나는 Selector 요소와 일치

$(Selector[attr *= ”value”]) 
attr 속성의 값이 value 값을 포함하는 Selector 요소와 일치

$(Selector[attr ~= ”value”]) 
attr 속성의 값이 공백과 함께 value 값을 포함하는 Selector 요소와 일치




**------------- 이벤트 핸들러 ---------------------**

$("선택자").bind(); // 이벤트 묶기
$("선택자").unbind(); // 이벤트 해제
$("선택자").click(); // 버튼클릭 = onclick
$("선택자").change(); // 텍스트박스의 값이 변결될때 = onchange
$("선택자").dbclick(); //더블클릭
$("선택자").focus(); //포커스가 주어질 때
$("선택자").keydown(); //키보드가 눌려 있을때
$("선택자").keyup(); //키보드가 눌렀다 떼었을때
$("선택자").keypress(); //키보드가 눌리는 순간
$("선택자").load(); //페이지를 전부 다 읽어들인 후에
$("선택자").hover( 오버시 실행함수, 아웃시 실행함수); //롤로버 이벤트핸들러
$("선택자").mousedown(); //마우스버튼 눌렀을때
$("선택자").mouseenter(); //객체영역에 마우스가 위치했을때
$("선택자").mouseleave(); //객체영역에서 마우스가 벗어났을때
$("선택자").mousemouse(); //
$("선택자").mouseout(); //마우스 커서가 올려놓았다가 밖으로 나갈때
$("선택자").mouseover(); //마우스 커서를 올려놓았을때
$("선택자").mouseup(); //마우스버튼 눌렀다 떼었을때
$("선택자").scroll(); //스크롤바가 스클로될때
$("선택자").trigger();
$("선택자").live();

$("선택자").rotate({
'duration' : '1000', //이동속도
'interval' : 2000, //1000 = 1초
'stopButton' : '#stopButton', //스톱버튼 (객체명)
'playButton' : '#playButton', //재생버튼 (객체명)
'prevButton' : '#prevButton', //이전버튼 (객체명)
'nextButton' : '#nextButton', //다음버튼 (객체명)
'movement' : 'top', // left, top , opacity
'autoStart' : true // 시작시 자동재생
});



**--------- 속성 ----------------**

$("선택자").attr("속성명","속성값"); //속성 값을 지정할때
$("선택자").attr("속성명"); //속성 값을 불러올때
$("선택자").removeAttr("속성명"); //속성을 삭제할때
$("선택자").val(); //객체의 값(value)을 가져올때
$("선택자").val("50"); //객체에 값(value)을 을 50으로 적용
$("선택자").text(); //객체의 텍스트를 가져온다.
$("선택자").html(); //객체의 HTML태그를 가져온다.
$("선택자").html("<p>나는 천재다.</p>"); //HTML태그를 삽입한다.
$("선택자").addClass("클래스명"); //객체에 클래스를 추가한다.
$("선택자").removeClass("클래스명"); //객체의 클래스를 삭제한다.
$("선택자").toggleClass("클래스명"); //객체에 해당클래스가 있으면 삭제, 없으면 추가 
$("선택자").css("스타일 속성 명","스타일 속성 값"); //CSS의 속성값을 지정
$("선택자").css({"background":"yellow","height":"400px"}); //CSS 다중 지정
$("선택자").css("스타일 속성 명"); //CSS 속성 값을 불러옴.
$("선택자").width();
$("선택자").index(this); //배열객체중 현재 선택된 인덱스 값 



|             | getter 메소드와 setter 메소드                                |
| :---------- | :----------------------------------------------------------- |
| .html()     | 해당 요소의 HTML 콘텐츠를 반환하거나 설정한다.               |
| .text()     | 해당 요소의 텍스트 콘텐츠를 반환하거나 설정한다.             |
| .width()    | 선택한 요소 중에서 첫 번째 요소의 너비를 픽셀 단위의 정수로 반환하거나 설정한다. |
| .height()   | 선택한 요소 중에서 첫 번째 요소의 높이를 픽셀 단위의 정수로 반환하거나 설정한다. |
| .attr()     | 해당 요소의 명시된 속성의 속성값을 반환하거나 설정한다.      |
| .position() | 선택한 요소 중에서 첫 번째 요소에 대해 특정 위치에 존재하는 객체를 반환한다. (getter 메소드) |
| .val()      | ``요소의 값을 반환하거나 설정한다.                           |




------------ **메소드 모음** --------------------

$("선택자1").add("선택자2").css("background-color","yellow"); //선택자1,선택자2 추가하여 css 공통 선언

$("선택자").ready(function(){...}); //페이지를 읽어들인 후에 함수 실행
$("선택자").hide(); //감추기
$("선택자").show(); //보이기
$("선택자").toggle(); //감추어진것은 보이고, 보여진것은 감추는 토글모드
$("선택자").fadeOut(); //서서히 감춰지기
$("선택자").slideDown(100); //0.1초 동안 슬라이드로 내려오면서 보이기
$("선택자").slideUp(100); //0.1초 동안 슬라이드로 올라가면서 감추기
$("선택자").slideToggle(); //감추어진것은 내려오면서 보이고, 보여진것은 올라가면서 감추어지기 (토글모드)


$(선택자1).prepend(선택자2) -> 선택자1 자식요소 앞에 선택자2를 넣어라.

$(선택자2).prependTo(선택자1) -> 선택자2를 선택자1 자식요소 앞에 넣어라.

 

$(선택자1).append(선택자2) -> 선택자1 자식요소 뒤에 선택자2를 넣어라.

$(선택자2).appendTo(선택자1) -> 선택자2를 선택자1 자식요소 뒤에 넣어라.


$(선택자1).before(선택자2) -> 선택자1 요소 앞에 선택자2를 넣어라.

$(선택자2).insertBefore(선택자1) -> 선택자2를 선택자1 요소 앞에 넣어라.

 

$(선택자1).after(선택자2) -> 선택자1 요소 뒤에 선택자2를 넣어라.

- [![페이스북으로 보내기](http://bamtol.net/v5/plugin/sns/icon/facebook.png)](http://bamtol.net/v5/bbs/sns_send.php?longurl=http%3A%2F%2Fbamtol.net%2Fv5%2Fbbs%2Fboard.php%3Fbo_table%3Dpp_js%26wr_id%3D18&title=제이쿼리+-+선택자%2C++이벤트핸들러%2C+속성%2C+메소드+모음&sns=facebook)
- [![트위터로 보내기](http://bamtol.net/v5/plugin/sns/icon/twitter.png)](http://bamtol.net/v5/bbs/sns_send.php?longurl=http%3A%2F%2Fbamtol.net%2Fv5%2Fbbs%2Fboard.php%3Fbo_table%3Dpp_js%26wr_id%3D18&title=제이쿼리+-+선택자%2C++이벤트핸들러%2C+속성%2C+메소드+모음&sns=twitter)
- [![구글플러스로 보내기](http://bamtol.net/v5/plugin/sns/icon/gplus.png)](http://bamtol.net/v5/bbs/sns_send.php?longurl=http%3A%2F%2Fbamtol.net%2Fv5%2Fbbs%2Fboard.php%3Fbo_table%3Dpp_js%26wr_id%3D18&title=제이쿼리+-+선택자%2C++이벤트핸들러%2C+속성%2C+메소드+모음&sns=gplus)

- [이전글](http://bamtol.net/v5/bbs/board.php?bo_table=pp_js&wr_id=19)
- [다음글](http://bamtol.net/v5/bbs/board.php?bo_table=pp_js&wr_id=16)

- [목록](http://bamtol.net/v5/bbs/board.php?bo_table=pp_js&page=)

[![밤톨넷 하단마크](http://bamtol.net/v5/img/footer_logo.png)](http://bamtol.net/v5/)

- [밤톨생각](http://bamtol.net/v5/bbs/board.php?bo_table=bt_mind)
- [취미생활](http://bamtol.net/v5/bbs/board.php?bo_table=bt_aqua)
- [Portfolio](http://bamtol.net/v5/bbs/board.php?bo_table=bt_portfolio)
- [메일문의](http://bamtol.net/v5/inc/bamtol_mail.php?mem=)

[ ](http://bamtol.net/v5/bbs/login.php)**밤톨.넷**®의 모든 내용은 얼마든지 무료로 활용이 가능합니다. 단, 내용을 다른 곳에 무단 게시하는 것은 금합니다. 스크랩을 원하시면 출처를 표시하거나 게시글 하단 SNS공유를 활용바랍니다. [[ **모바일 버전으로 보기** \]](http://bamtol.net/v5/bbs/board.php?bo_table=pp_js&wr_id=18&device=mobile)

