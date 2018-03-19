#1주차

## project만들기
    * Create Project를 누르세요
    * 경로설정을 해야합니다.

    * c:\git\python\python_practice_01

    * 우측 하단 Create
    * 그러면 파이썬이 빌드를 합니다.
    * 빌드가 완료되면 왼쪽에 project explorer가 나옵니다.
    * 왼쪽에 파일이 보이는 부분을 project explorer라고 합니다.

    * python_practice_01이라고 되어있는 부분이
    * project root입니다.

## package만들고 python파일 만들기
    * 오른쪽 버튼을 눌러서 context menu를 엽니다.
    * 마우스 오른쪽 버튼을 누르면 나오는 메뉴가 context메뉴 입니다.

    * New -> python package 선택합니다.

    * package이름을 com으로 합니다.
    * package는 폴더라고 생각하시면 됩니다.

    * 폴더(package)를 만들고 python파일을 만듭니다.
    * 만든 package에서 context menu를 호출 합니다.
    * new -> python file
    * 파일명 01_hello

## 실행 방법
    * run -> run
    * hello가 출력 되는 부분이 console 입니다.


## function(함수)이란?
    * 펑션으로 읽는다. 함수로 번역 해놓았다.
    * f, fn, f(x)
    * python의 모든 기능들은 function으로 되어있다.
    * 값을 넣으면 특정 로직을 실행하고 때로는 결과값을 알려준다.


## Function(함수)만들기
<pre>
    def print_hello():
        print("hello")
</pre>
    * def로 시작한다.
    * def옆에 한칸을 띄운다
    * 그 옆에는 이름이 나온다.
    * 이름은 아무거나 가능하다. ex)aaaa, bbb, plus, minus
    * 이름 옆에는 ()를 붙인다.
    * ()옆에는 :를 붙인다.
    * 엔터를 친다.
    * tab을 넣는다
    * 넣고 싶은 기능을 코딩한다. ex) print("hello")

    * 들여쓰기가 들어가지 않은 줄이 나올때까지를 function 으로 봅니다.


## parameter란?
    * 파라메터로 읽는다. 매개변수로 번역 되었다.
    * 함수를 호출 할 때 함수로 값을 넘겨줄 때 사용한다.
    * 파라메터는 여러개를 만들 수 있다.

## return이란?
    * 리턴이라고 읽는다. 돌려준다 반환한다 등으로 번역되었다.
    * 함수를 실행한 결과를 함수를 호출한 곳으로 보내준다.
    * 왜 쓰냐면 연산한 결과를 다른곳에 사용하기 위함
    * 처음에 console만 보면 동일해서 헷갈림.

# 실습
## week1
0. bye를 출력하는 함수 만들기
1. plus, minus, multiple, divide 함수 만들기(사칙연산)
    - 숫자 2개를 입력 받는 함수 4개를 만듭니다.
2. 0~99까지 숫자 만들기 arange
3. filter이용해서 80보다 큰 숫자 콘솔에 출력하기
4. data만들고 matplot으로 chart그리기
5.format()을 넣고 데이터 바로 가공 해보기 '00는 00입니다.'

# week2
1.구구단 2단 출력하기
2.구구단 2, 3단 출력하기
3.구구단 2 ~ 9단 출력하기

# week2 이론
url : 인터넷 주소
http : 인터넷 주소 앞에 붙는 것 protocol
html : 인터넷에서 문서를 보여줄때 쓰는 표현식들
server : 페이지를 서빙해주는 곳 (naver, google)


5. matplot으로 차트 그리기
6. 1~10까지 우상향 하는 그래프를 그려보세요
7. sin그래프 그리기
8. sin, cos그래프 한번에 그리기
9. linspace 사용하기
10. y = x 함수 그래프로 그리기
11. y = x + 1 그래프로 그리기
12. 함수 x2는 x + 1인 함수를 만들어 보세요

13.pandas.DataFrame.to_csv로 dta 를 csv로 바꾸기
14.pandas.read_csv로 csv읽어오기
