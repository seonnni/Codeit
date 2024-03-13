## 프로그래밍과 데이터 in Python
# 1. 리스트(list)
numbers = [2, 3, 5, 7, 11, 13]
names = ["윤수", "혜린", "태호", "영훈"]

print(numbers)
print(names)

# 인덱싱 (indexing)
print(names[0])

print(numbers[1]+numbers[3])

num_1 = numbers[1]
num_3 = numbers[3]
print(num_1+num_3)

print(numbers[-1])

# 리스트 슬라이싱(list slicing)
print(numbers[0:4]) #인덱스 0 ~ 3!!
print(numbers[2:]) #인덱스 2 ~ 끝까지
print(numbers[:3]) #맨 앞에서부터 2까지

new_list = numbers[:3] # [2,3,5]
print(new_list[2])

# 요소 바꾸기
numbers[0] = 7
print(numbers)

numbers[0] = numbers[0] + numbers[1]
print(numbers)

# 2. 리스트 함수
numbers = []
numbers.append(5) # 새로운 값을 리스트의 가장 오른쪽에 추가(추가 연산)
numbers.append(8)
print(numbers)
print(len(numbers)) #요소가 몇개 인지 알고 싶으면

numbers = [2, 3, 5, 7, 11, 13, 17, 19]
del numbers[3] #리스트 삭제 (7 삭제제)
print(numbers)
numbers.insert(4, 37) #4번 인덱스에 정수 37을 삽입(삽입 연산)
print(numbers)

# 3. 리스트 정렬
numbers = [19, 13, 2, 5, 3, 11, 7, 17]

new_list = sorted(numbers)
print(new_list)
new_list_reverse = sorted(numbers, reverse = True)
print(new_list_reverse)

print(numbers.sort()) #None
print(numbers)

# sorted(함수) : 기존 리스트는 건드리지 않고, 정렬된 새로운 리스트를 리턴
# sort : 아무것도 리턴하지 않고, 기존 리스트를 정렬

#4. 리스트 인덱싱 연습
greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]

# 여기에 코드를 작성하세요
i = 0
while i <=6:
    print(greetings[i])
    i += 1
    
# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(fahrenheit):
    # 여기에 코드를 작성하세요
    return (fahrenheit - 32) * 5 / 9


temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: {}".format(temperature_list))  # 화씨 온도 출력

# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드를 입력하세요
i = 0
while i <= 5:
    temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]),1)
    i += 1
print("섭씨 온도 리스트: {}".format(temperature_list))  # 섭씨 온도 출력

# 원화(￦)에서 달러($)로 변환하는 함수
def krw_to_usd(krw):
    # 여기에 코드를 작성하세요
    return krw / 1000

# 달러($)에서 엔화(￥)로 변환하는 함수
def usd_to_jpy(usd):
    # 여기에 코드를 작성하세요
    return usd * 125

# 원화(￦)으로 각각 얼마인가요?
prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(prices))
 
# prices를 원화(￦)에서 달러($)로 변환하기
# 여기에 코드를 작성하세요
i = 0
while i <= 7:
    prices[i] = round(krw_to_usd(prices[i]),1)
    i += 1
# 달러($)로 각각 얼마인가요?
print("미국 화폐: " + str(prices))

# prices를 달러($)에서 엔화(￥)으로 변환하기
# 여기에 코드를 작성하세요
k = 0
while k <= 7:
    prices[k] = round(usd_to_jpy(prices[k]),1)
    k += 1
# 엔화(￥)으로 각각 얼마인가요?
print("일본 화폐: " + str(prices))

# 빈 리스트 만들기
numbers = []
print(numbers)

# numbers에 값들 추가
# 코드를 입력하세요
numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)
print(numbers)

# numbers에서 홀수 제거
# 코드를 입력하세요
i = 0
while i < len(numbers):
    if numbers[i] % 2 != 0:
        del numbers[i]
    else :
        i += 1
print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
# 코드를 입력하세요
numbers.insert(0, 20)
print(numbers)

# numbers를 정렬해서 출력
# 코드를 입력하세요
numbers.sort()
print(numbers)

# 리스트에서 값의 존재 확인하기
# value가 some_list의 요소인지 확인
def in_list(some_list, value):
    i = 0
    while i < len(some_list):
        # some_list에서 value를 찾으면 True를 리턴
        if some_list[i] == value:
            return True
        i = i + 1

    # 만약 some_list에서 value를 발견하지 못했으면 False를 리턴
    return False

# 테스트
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(in_list(primes, 7))
print(in_list(primes, 12))

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 in primes)
print(12 in primes)

# 값이 없는지 확인
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 not in primes)
print(12 not in primes)

# 리스트 안의 리스트 (Nested List)
# 세 번의 시험을 보는 수업
grades = [[62, 75, 77], [78, 81, 86], [85, 91, 89]]

# 첫 번째 학생의 성적
print(grades[0])

# 세 번째 학생의 성적
print(grades[2])

# 첫 번째 학생의 첫 번째 시험 성적
print(grades[0][0])

# 세 번째 학생의 두 번째 시험 성적
print(grades[2][1])

# 첫 번째 시험의 평균
print((grades[0][0] + grades[1][0] + grades[2][0]) / 3)

# sort 메소드
numbers = [5, 3, 7, 1]
numbers.sort()
print(numbers)

# reverse 메소드(뒤집어진 순서로 배치)
numbers = [5, 3, 7, 1]
numbers.reverse()
print(numbers)

# index 메소드
members = ["영훈", "윤수", "태호", "혜린"]
print(members.index("윤수"))
print(members.index("태호"))

# remove 메소드
fruits = ["딸기", "당근", "파인애플", "수박", "참외", "메론"]
fruits.remove("파인애플")
print(fruits)

# 1. for 반복문
my_list = [2,3, 5, 7, 11]

for number in my_list:
    print(number)

# 2. range 함수
for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)
# 파라미터 2개 버전
for i in range(start, stop):
    print(i)
for i in range(3,11): # 3부터 10까지!
    print(i)
# 파라미터 1개 버전
for i in range(stop):
     print(i)
for i in range(10): # 0부터 9까지
    print(i)
# 파라미터 3개 버전
for i in range(start, stop, step):
    print(i)
for i in range(3,17,3): # 3부터 17까지 3씩 간격격
    print(i)
# range 함수의 장점 : 간편하고 깔끔함, 메모리 효율성

# 3. range 연습
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# 인덱스와 원소 출력
# 여기에 코드를 작성하세요
for i in range(11):
    print(i, numbers[i])
    
# 4. 거듭제곱
for i in range(11):
    print("2^{} = {}".format(i,2**i))
    
# 5. for문으로 구구단
for j in range(1,10):
    for i in range(1,10):
        print("{} * {} = {}".format(j, i, i*j))
        
# 6. 피타고라스 삼조
for a in range(1, 400):
    for b in range(1, 400):
        c = 400 - a - b
        if a * a + b * b == c * c and a < b < c and a + b + c == 400:
            print(a * b * c)

# 7. 리스트 뒤집기
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
# 여기에 코드를 작성하세요
numbers.reverse()

print("뒤집어진 리스트: " + str(numbers))

# 1. 사전 (dictionary)
# key-value pair (키-값 쌍)
my_list = [2, 3, 5, 7, 11, 13]
print(my_list[1])
print(my_list[3])

my_dictionary = {
    5: 25,
    2: 4,
    3: 9
}
print(type(my_dictionary))
print(my_dictionary[3])
# 새로운 쌍 추가
my_dictionary[9] = 81
print(my_dictionary)
# 사전은 리스트와 다르게 순서의 개념이 없음
# 리스트의 인덱스는 0,1,2 같이 정수형인데 사전은 정수형일 필요가 없음
my_family = {
    '엄마': '김자옥',
    '아빠': '이석진',
    '아들': '이동민',
    '딸': '이지영'
}
print(my_family['아빠'])

# 1. 단어장 만들기
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명'
}
print(vocab)


# 2. 새로운 단어들 추가
vocab['privilege'] = '특권'
vocab['principle'] = '원칙'
print(vocab)

# 3. 사전 활용법
my_family = {
    '엄마': '김자옥',
    '아빠': '이석진',
    '아들': '이동민',
    '딸': '이지영'
}

print('이지영' in my_family.values())

for value in my_family.values():
    print(value)
    
print(my_family.keys())
for key in my_family.keys():
    value = my_family[key]
    print(key, value)
    
for key, value in my_family.items():
    print(key, value)
    
# 언어 사전의 단어와 뜻을 서로 바꿔주는 함수
def reverse_dict(dict):
    new_dict = {}  # 새로운 사전
    for key, value in dict.items():
        
        new_dict[value] = key
    # dict의 key와 value를 뒤집어서 new_dict에 저장
    # 여기에 코드를 작성하세요
    return new_dict  # 변환한 새로운 사전 리턴


# 영-한 단어장
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
}

# 기존 단어장 출력
print("영-한 단어장\n{}\n".format(vocab))

# 변환된 단어장 출력
reversed_vocab = reverse_dict(vocab)
print("한-영 단어장\n{}".format(reversed_vocab))

# 투표 결과 리스트
votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', \
'최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기', \
'강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']

# 후보별 득표수 사전
vote_counter = {}

# 리스트 votes를 이용해서 사전 vote_counter를 정리하기
for name in votes :
    if name not in vote_counter:
        vote_counter[name] = 1
    else :
        vote_counter[name] += 1
# 후보별 득표수 출력
print(vote_counter)

# 1. Aliasing
x = 5
y = x
y = 3
print(x)
print(y)

x = [2, 3, 5, 7, 11]
y = x
y[2] = 4
print(x)
print(y)

x = [2, 3, 5, 7, 11]
y = list(x)
y[2] = 4
print(x)
print(y)

# 3. 리스트와 문자열
alphabet_list = ['A','B','C','D','E','F','G','H','I','J']

print(alphabet_list[0])
print(alphabet_list[1])
print(alphabet_list[4])
print(alphabet_list[-1])

alphabet_string = 'ABCDEFGHJ'
print(alphabet_string[0])
print(alphabet_string[1])
print(alphabet_string[4])
print(alphabet_string[-1])

print(alphabet_list[0:5])
print(alphabet_list[4:])
print(alphabet_list[:4])

print(alphabet_string[0:5])
print(alphabet_string[4:])
print(alphabet_string[:4])

str_1 = 'Hello'
str_2 = 'World'
str_3 = str_1 + str_2
print(str_3)

list_1 = [1,2,3,4]
list_2 = [5,6,7,8]
list_3 = list_1 + list_2
print(list_3)

my_list = [2,3,5,7,11]
print(len(my_list))

my_string = 'Hello World!'
print(len(my_string))

# 리스트와 문자열의 차이점
numbers = [1,2,3,4]
numbers[0] = 5
print(numbers)

name = 'codeit'
name[0] = 'C'
print(name) # 문자열은 리스트와 달리 수정할 수 없음

# 리스트와 문자열 정리
# 인덱싱(indexing) : 두 자료형은 공통적으로 인덱싱이 가능합니다.
# 알파벳 리스트의 인덱싱
alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabets_list[0])
print(alphabets_list[1])
print(alphabets_list[4])
print(alphabets_list[-1])

# 알파벳 문자열의 인덱싱
alphabets_string = 'ABCDEFGHIJ'
print(alphabets_string[0])
print(alphabets_string[1])
print(alphabets_string[4])
print(alphabets_string[-1])

# for 반복문 :  두 자료형은 공통적으로 인덱싱이 가능합니다. 따라서 for 반복문에도 활용할 수 있습니다.
# 알파벳 리스트의 반복문
alphabets_list = ['C', 'O', 'D', 'E', 'I', 'T']
for alphabet in alphabets_list:
    print(alphabet)

# 알파벳 문자열의 반복문
alphabets_string = 'CODEIT'
for alphabet in alphabets_string:
    print(alphabet)

# 슬라이싱(Slicing): 두 자료형은 공통적으로 슬라이싱이 가능합니다.
# 알파벳 리스트의 슬라이싱
alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabets_list[0:5])
print(alphabets_list[4:])
print(alphabets_list[:4])

# 알파벳 문자열의 슬라이싱
alphabets_string = 'ABCDEFGHIJ'
print(alphabets_string[0:5])
print(alphabets_string[4:])
print(alphabets_string[:4])

# 덧셈 연산 :  두 자료형에게 모두 덧셈은 "연결"하는 연산입니다.
# 리스트의 덧셈 연산
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = list1 + list2
print(list3)

# 문자열의 덧셈 연산
string1 = '1234'
string2 = '5678'
string3 = string1 + string2
print(string3)

# len 함수 : 두 자료형은 모두 길이를 재는 len 함수를 쓸 수 있습니다.
# 리스트의 길이 재기
print(len(['H', 'E', 'L', 'L', 'O']))

# 문자열의 길이 재기
print(len("Hello, world!"))

# Mutable (수정 가능) vs. Immutable (수정 불가능)
# 리스트 데이터 바꾸기
numbers = [1, 2, 3, 4]
numbers[0] = 5
print(numbers)

# 문자열 데이터 바꾸기
name = "codeit"
name[0] = "C"
print(name) # error

# 자리수 합 리턴
def sum_digit(num):
    total = 0
    str_num = str(num)
    
    for digit in str_num:
        total += int(digit)
        
    return total

# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
# 여기에 코드를 작성하세요
hap = 0
for i in range(1,1001):
    hap += sum_digit(i)
print(hap)

# 주민등록번호 가리기
star = '****'
def mask_security_number(security_number):
    str_num = security_number[:-4] + star
    return str_num
    
# 테스트 코드
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))

# 7. 팰린드롬
def is_palindrome(word):
    # 여기에 코드를 작성하세요
    for i in range(len(word)):
        if word[i] == word[len(word) -i - 1]:
            pass
        else:
            return False
    return True

# 테스트 코드
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))