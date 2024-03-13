## 프로그래밍 핵심 개념 in Python
## [1] 자료형
# 1. 숫자형
print(4+7) #덧셈
print(2-4) #뺄셈
print(5*3) #곱셈
print(7%3) #나머지
print(2**3) #거듭제곱

print(4.0+7.0) # 소수형

print(4+7.0) # 정수형+소수형 = 소수형(소수가 더 쎄다~)

print(7/2) #나누기 - 항상 소수형형
print(6/2)
print(7.0/2)
print(6.0/2.0)

print(2+3*2) #사칙연산 따른다
print(2*(2+3))

# 2. 숫자형 심화
#floor division(버림 나눗셈)
print(7//2) #소수 부분을 버리고 몫만 출력
print(8//3)
print(8.0//3) #둘 중 하나가 소수면 소수로 출력(=2.0)
print(8//3.0)
print(8.0//3.0)

#round 함수(반올림)
print(round(3.1415926535))
print(round(3.1415926535,2)) #둘째 자리에서 반올림

# 3. 문자열(키보드로 쓸 수 있는 문자들을 표현하는 자료형)
# 문자열 연결(문자열 덧셈, String Concatenation)

print("코드잇")
print("유재석")
print('I'm excited to learn Python!) # -> 오류
print("I'm excited to learn Python!")
print("I\'m \"excited\" to learn Python!")

print("Hello"+"World")
print("Hello"*3)
print("3"+"5") #35

# 6. 형 변환(Type Conversion,값을 한 자료형에서 다른 자료형으로 바꾸는 것)
print(int(3.8)) #정수형으로 변환
print(float(3)) #소수형으로 변환
print(int("2")+int("5")) #문자형을 정수형으로 변환
print(float("1.1")+float("2.5"))
print(str(2)+str(5)) # 정수를 문자열로 변환
age = 7
print("제 나이는" +str(age)+ "살입니다.")
print(int("Hello world!")) # -> x(논리적으로 불가능)

# 8. format을 이용한 문자열 포매팅
# 오늘은 2019년 10월 29일입니다.
year = 2019
month = 10
day = 29

print("오늘은 "+str(year)+"년 "+str(month)+"월 "+str(day)+"일입니다.")

date_string="오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year,month,day))
print("오늘은 {}년 {}월 {}일입니다.".format(year, month, day+1))

# 9. format 다루기
print("저는 {1},{0},{2}를 좋아합니다!".format("박지성","유재석","빌 게이츠"))

num_1 = 1
num_2 = 3
print("{0} 나누기 {1}은 {2: .2f}입니다.".format(num_1,num_2,num_1 / num_2))

# 가장 오래된 방식
name = "최지웅"
age = 32
print("제 이름은 %s이고 %d살입니다." % (name, age))
# 현재 가장 많이 쓰는 방식
name = "최지웅"
age = 32
print("제 이름은 {}이고 {}살입니다.".format(name, age))
# 새로운 방식
name = "최지웅"
age = 32
print(f"제 이름은 {name}이고 {age}살입니다.")

##실습
wage = 5  # 시급 (1시간에 5달러)
exchange_rate = 1142.16  # 환율 (1달러에 1142.16원)

# "1시간에 5달러 벌었습니다." 출력
print("{}시간에 {}{} 벌었습니다.".format(1, wage * 1, "달러"))

# "5시간에 25달러 벌었습니다." 출력
print("{}시간에 {}{} 벌었습니다.".format(5, wage * 5, "달러"))  # 여기에 코드를 작성하세요

# "1시간에 5710.8원 벌었습니다." 출력
print("{}시간에 {:.1f}{} 벌었습니다.".format(1, exchange_rate * 5, "원"))  # 여기에 코드를 작성하세요

# "5시간에 28554.0원 벌었습니다." 출력
print("{}시간에 {:.1f}{} 벌었습니다.".format(5, exchange_rate * 25, "원"))  # 여기에 코드를 작성하세요

# 12. 불 대수(일상적인 논리를 수학적으로 표현한 것, 진리값(참,거짓))
# 불 대수의 연산 : and or not
# and 연산 (x와 y가 모두 참일 때만 x and y가 참)
# and 예시 : 대한민국의 수도는 서울이다 and 2는 1보다 크다
# or 연산 (x와 y중 둘 중 하나라도 참이면 x or y는 참)
# or 예시 : 대한민국의 수도는 서울이다 or 대한민국의 수도는 제주도이다
# not 연산
# not 예시 : not 대한민국의 수도는 서울이다 -> false

#13. 불린(Boolean)형
print(True)
print(False)

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not True)
print(not False)

print(2>1)
print(2<1)
print(3>=2)
print(3<=3)
print(2==2)
print(2!=2)

print("Hello"=="Hello")
print("Hello"!="Hello")
print(2>1 and "Hello"=="Hello") #True and True
print(not not True)
print(not not False)

print(7==7 or(4<3 and 12>10))
x=13
print(x>4 or not(x<2 or x==3))

# 14. type 함수
print(type(3))
print(type(3.0))
print(type("3"))
print(type("True"))
print(type(True))

def hello():
    print("Hello world!")
print(type(hello))
print(type(print))

## [2] 추상화
# 1. 변수 제대로 이해하기
name = "김현승"
x = 7
x = x+1 # 파이썬에서 =는 지정연산자(오른쪽을 왼쪽에 넣어라)
x = x-3

#2. 함수의 실행 순서
def hello():
    print("Hello!")
    print("Welcome to Codeit!")

print("함수 호출 전")
hello()
print("함수 호출 후")

def square(x):
    return x*x

print("함수 호출 전")
print(square(3) +square(4))
print("함수 호출 후")

# 3. return문(함수가 무언가를 돌려주는 것) 제대로 이해하기
#return문의 역할
# 1. 값 돌려주기
# 2. 함수 즉시 종료하기기
def square(x):
    print("함수의 시작")
    return x*x
    print("함수의 끝") #dead code(의미 없는 코드드)
    
print(square(3))
print("Hello World!")

# 4. return과 print의 차이
def print_square(x):
    print(x*x)
    
def get_square(x):
    return x*x
    
print_square(3)
get_square(3) #대체되기만 하고 출력은 안됨
print(get_square(3))
print(print_square(3)) #return이 없으면 none으로 대체

# 6. 옵셔널 파라미터(파라미터에 기본값 설정)
def myself(name, age, nationality="한국"):
    print("내 이름은 {}".format(name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))


myself("코드잇", 1, "미국")  # 옵셔널 파라미터를 제공하는 경우
print()
myself("코드잇", 1)  # 옵셔널 파라미터를 제공하지 않는 경우

# 옵셔널 파라미터는 모두 마지막에 있어야 한다!
def myself(name, nationality="한국", age):
    print("내 이름은 {}".format(name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))


myself("코드잇", 1)  # 기본값이 설정된 파라미터를 바꾸지 않을 때
print()
myself("코드잇", "미국", 1)  # 기본값이 설정된 파라미터를 바꾸었을 때

# 7. Syntactic Sugar(자주 쓰이는 표현을 더 간략하게 쓸 수 있게 하는 문법)
# 다음 두 줄은 같습니다
x = x + 1
x += 1

# 다음 두 줄은 같습니다
x = x + 2
x += 2

# 다음 두 줄은 같습니다
x = x * 2
x *= 2

# 다음 두 줄은 같습니다
x = x - 3
x -= 3

# 다음 두 줄은 같습니다
x = x / 2
x /= 2

# 다음 두 줄은 같습니다
x = x % 7
x %= 7

# 9. scope(범위)
x = 2 #글로벌 변수(함수 밖에 정의, 모든 곳에서 사용 가능)
def my_function():
    x=3 #로컬변수(이 함수 내에서만 사용 가능)
    print(x)
    
my_function()
print(x) #-> 오류(x가 정의되지 않음)

#파라미터도 로컬 변수!
def square(3):
    return x*x
    
print(square(3)) #-> 오류

#scope : 변수가 사용 가능한 범위
# 로컬 변수 : 변수를 정의한 함수 내에서만 사용 가능
# 글로벌 변수 : 모든 곳에서 사용 가능
# 함수에서 변수를 사용하면, 로컬 변수를 먼저 찾고 나서 글로벌 변수를 찾음

# 11. 상수(constant, 절대로 바뀌지 않는 값)
# 규칙 : 모든 글자를 대문자로!
PI = 3.14 # 원주율 '파이'

# 반지름을 받아서 원의 넓이 계산
def calculate_area(r):
    return PI*r*r
    
radius = 4
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 6
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 7
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

# 12. 스타일
# 버거를 주문할 시에 혜택 차원에서 음료수 및 감자튀김을 받을 수 있다
# vs.
# 버거를 주문하면 음료수와 감자튀김은 서비스다.
# 이해하기 쉬운 코드 =  좋은 스타일을 가진 좋은 코드

# 원의 둘레와 넓이
print(6.28*4)
print(3.14*4*4)
print(6.28*8)
print(3.14*8*8)

a=3.14 #원주율(파이)
b=4 #반지름
print(2*a*b)
print(a*b*b)
b=8 #반지름
print(2*a*b)
print(a*b*b)

# 좋은 코드
PI = 3.14 #원주율(파이)

# 반지름이 r인 원의 둘레 계산
def calculate_circumference(r):
    return 2 * PI * r
    
# 반지름이 r인 원의 넓이이 계산
def calculate_area(r):
    return PI * r * r
    
radius = 4 #반지름
print(calculate_circumference(radius))
print(calculate_area(radius))

radius = 8 #반지름
print(calculate_circumference(radius))
print(calculate_area(radius))

# 13.파이썬 스타일 가이드 (PEP 8)
# 이름 규칙(모든 변수와 함수 이름은 소문자로 쓰고, 여러 단어일 경우 _로 나눠주세요.)
# bad
someVariableName = 1
SomeVariableName = 1

def someFunctionName():
    print("Hello")
    
# good
some_variable_name = 1

def some_function_name():
    print("Hello")

# 모든 상수 이름은 대문자로 쓰고, 여러 단어일 경우 _로 나눠주세요.
# bad
someConstant = 3.14
SomeConstant = 3.14
some_constant = 3.14

# good
SOME_CONSTANT = 3.14

# 의미 있는 이름(변수)
# bad (의미 없는 이름)
a = 2
b = 3.14
print(b * a * a)
# good (의미 있는 이름)
radius = 2
PI = 3.14
print(PI * radius * radius)

# 의미 있는 이름(함수)
# bad (의미 없는 이름)
def do_something():
    print("Hello, world!")

# good (의미 있는 이름)
def say_hello():
    print("Hello, world!")
    
# 화이트 스페이스
# 들여쓰기(들여쓰기는 무조건 스페이스 4개를 사용하세요.)
# bad (스페이스 2개)
def do_something():
  print("Hello, world!")
# bad (스페이스 8개)
i = 0
while i < 10:
        print(i)
# good (스페이스 4개)
def say_hello():
    print("Hello, world!")
    
# 함수 정의(함수 정의 위아래로 빈 줄이 두 개씩 있어야 합니다. 하지만 파일의 첫 줄이 함수 정의인 경우 해당 함수 위에는 빈 줄이 없어도 됩니다.)
#)
# bad
def a():
    print('a')
def b():
    print('b')

def c():
    print('c')
# good
def a():
    print('a')


def b():
    print('b')


def c():
    print('c')
    
# 괄호 안 (괄호 바로 안에는 띄어쓰기를 하지 마세요.)
# bad
spam( ham[ 1 ], { eggs: 2 } )
# good
spam(ham[1], {eggs: 2})

# 함수 괄호(함수를 정의하거나 호출할 때, 함수 이름과 괄호 사이에 띄어쓰기를 하지 마세요.)
# bad
def spam (x):
    print (x + 2)


spam (1)
# good
def spam(x):
    print(x + 2)


spam(1)

# 쉼표(쉼표 앞에는 띄어쓰기를 하지 마세요.)
# bad
print(x , y)
# good
print(x, y)

# 지정 연산자 (지정 연산자 앞뒤로 듸어쓰기를 하나씩 넣어 주세요.)
# bad
x=1
x    = 1
# good
x = 1

# 연산자(기본적으로 연산자 앞뒤로 띄어쓰기를 하나씩 합니다.)
# bad
i=i+1
submitted +=1
# good
i = i + 1
submitted += 1

#하지만 연산의 '우선 순위'를 강조하기 위해서는, 연산자 앞뒤로 띄어쓰기를 붙이는 것을 권장합니다.
# bad
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)
# good
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)

# 코멘트 (일반 코드와 같은 줄에 코멘트를 쓸 경우, 코멘트 앞에 띄어쓰기 최소 두 개를 입력해 주세요.)
# bad
x = x + 1# 코멘트
# good
x = x + 1  # 코멘트

## 제어문
# 1. while 반복문 개념(무언가를 반복하기 위해 사용)
while 조건 부분:
    수행 부분
    
while 다운로드 안 받은 이미지가 있다:
    다음 이미지를 보고, 다운로드 받는다

# 2. while 반복문 문법
while 조건 부분(불린 값으로 계산되는 식):
    수행 부분(반복적으로 실행하고 싶은 명령)
while True:
    실행

i = 1
while  i <= 3 :
    print("나는 잘생겼다!")
    i += 1
    
# 3. while 반복문 실습 1
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
        i += 1
    else :
        i += 1
        
# 4. while 반복문 실습 2
i = 100

# 여기에 코드를 작성하세요
while True:
    if i % 23 == 0:
        print(i)
        break
    else :
        i += 1
        
# 5. if문 개념
while 다운로드 안 받은 이미지가 있다:
    다음 이미지를 본다
    if 이미지가 png 파일이다:
        이미지를 다운로드 받는다
    else:
        print("png가 아닙니다!")
        
# 6. if문 문법
if 조건 부분(불린 값으로 계산되는 식):
    수행 부분(조건을 충족했을 때, 실행하고 싶은 명령)

temperature = 8
if temperature <= 10:
    print("자켓을 입는다.")
else:
    print("자켓을 입지 않는다.")
    
# 7. elif문
if 점수가 90점 이상이다:
    A를 준다
elif 점수가 80점 이상이다:
    B를 준다
elif 점수가 70점 이상이다:
    C를 준다
elif 점수가 60점 이상이다:
    D를 준다
else:
    F를 준다
    
# 학점 계산기 
def print_grade(midterm_score, final_score):
    total = midterm_score + final_score
    # 여기에 코드를 작성하세요
    if total >= 90:
        print("A")
    elif total >= 80:
        print("B")
    elif total >= 70:
        print("C")
    elif total >= 60:
        print("D")
    else:
        print("F")
# 이상한 수학 문제 1
i = 1
while i <= 100:
    if i % 8 == 0 and i % 12 !=0:
        print(i)
        i += 1
    else :
        i += 1
        
# 이상한 수학 문제 2
i = 1
sum = 0
while i < 1000:
    if i % 2 == 0 or i % 3 == 0 :
        sum += i
        i += 1
    else :
        i += 1
print(sum)

# 약수 찾기
i = 120
n = 1
count = 0
while n <= 120:
    if i % n == 0:
        print(n)
        n += 1
        count += 1
    else:
        n += 1
print("120의 약수는 총 {}개 입니다.".format(count))

# 택이의 우승 상금
INTEREST_RATE = 0.12
APARTMENT_PRICE_2016 = 1100000000

year = 1988
bank = 50000000    

while year < 2016:
    bank = bank * (1 + INTEREST_RATE)
    year += 1
    
if bank > APARTMENT_PRICE_2016:
        minus = bank - APARTMENT_PRICE_2016
        print("{}원 차이로 동일 아저씨 말씀이 맞습니다".format(minus))
else :
        minus = APARTMENT_PRICE_2016 - bank
        print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(minus))
        
# 피보나치 수열
previous = 0
current = 1
i = 1

while i <= 50:
    print(current)
    temp = previous
    previous = current
    current = current + temp
    i += 1
    
# 구구단 만들기
k = 1
while k <= 9:
    i = 1
    while i <= 9:
        print("{} * {} = {}".format(k,i,k*i))
        i += 1 
    k += 1
    
# 제어문 꿀팁
# break 문
i = 100

while True:
    # i가 23의 배수면 반복문을 끝냄
    if i % 23 == 0:
        break
    i = i + 1

print(i)

# continue 문
i = 0

while i < 15:
    i = i + 1

    # i가 홀수면 print(i)하지 않고 바로 조건 부분으로 돌아감
    if i % 2 == 1:
        continue
    print(i)

