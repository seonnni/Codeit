## 파이썬 응용하기
# 1. 모듈
import calculator as calc

print(calc.add(2, 5))
print(calc.multiply(3, 4))

from calculator import add, multiply

print(add(2, 5))
print(multiply(3, 4))

# 2. 스탠다드 라이브러리(standard library, 표준 라이브러리)
import math

print(math.log10(100))
print(math.cos(0))
print(math.pi)

import random # 랜덤한 값을 만들고 싶을 때

print(random.random()) # 실행할 때마다 다른 값

import os # 파이썬으로 운영체제 조작

print(os.getlogin())
print(os.getcwd())

# 3. random 모듈
import random

# randint() 함수 : 두 수 사이의 어떤 랜덤한 정수를 리턴하는 함수
import random

print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))

# uniform() 함수 :  두 수 사이의 랜덤한 소수를 리턴
import random

print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))

# 4. daytime 모듈(날짜와 시간을 다루기 위한)
import datetime

# datetime 값 생성
pi_day = datetime.datetime(2020, 3, 14)
print(pi_day)
print(type(pi_day))

# 시간 설정
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(pi_day)
print(type(pi_day))

# 오늘 날짜
today = datetime.datetime.now()
print(today)
print(type(today))

# timedelta 타입(두 datetime 값 사이의 기간을 알고 싶으면 그냥 빼기)
today = datetime.datetime.now()
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(today - pi_day)
print(type(today - pi_day)) #timedelta 타입 :  날짜 간의 차이

today = datetime.datetime.now()
my_timedelta = datetime.timedelta(days=5, hours=3, minutes=10, seconds=50)

print(today)
print(today + my_timedelta) # 더할 수도 있다~

# datetime 해부하기 : '연도'나 '월' 같은 값들을 추출하려면?
today = datetime.datetime.now()

print(today)
print(today.year)  # 연도
print(today.month)  # 월
print(today.day)  # 일
print(today.hour)  # 시
print(today.minute)  # 분
print(today.second)  # 초
print(today.microsecond)  # 마이크로초

# datetime 포매팅 : strftime(), 이쁘게 쓰고 싶어용
today = datetime.datetime.now()

print(today)
print(today.strftime("%A, %B %dth %Y"))

# 1. input(사용자 입력을 받는다~)
name = input("이름을 입력하세요 : ")
print(name)

x = int(input(" 숫자를 입력하세요 :"))
print(x + 5)


import random

answer = random.randint(1, 20)
num_tries = 4
guess = -1
tries = 0


while guess != answer and tries < num_tries:
    input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(num_tries-tries))
    tries += 1
    if answer > guess:
        print("Up")
    elif answer < guess:
        print("Down")

if guess == answer:
    print("축하합니다. {}번만에 숫자를 맞히셨습니다.".format(tries))
        
else:
    print("아쉽습니다. 정답은 {}였습니다.".format(answer))
    
    
# 로또 시뮬레이션 : 번호 뽑기
import random

def generate_numbers(n):
    numbers = []

    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)

    return numbers

def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]
    
def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for num in numbers:
        if num in winning_numbers:
            count += 1
        else :
            pass
    return count

def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1 :
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000  


# 테스트 코드
print(generate_numbers(6))
print(draw_winning_numbers())
