# 1. 파일 읽기
with open('chicken.txt','r',encoding='UTF-8') as f:
    for line in f:
        print(line)


# 2. strip(화이트 스페이스를 없애주는 역할)
# 화이트 스페이스란? " ","\t","\n" 이런 공백들
print("Hello\n")
print("Hello")
print("        abc     def      ".strip())
print("   \t    \n     abc     def\n\n\n".strip())

with open('chicken.txt','r',encoding='UTF-8') as f:
    for line in f:
        print(line.strip())
        
# 3. split (나눈다)
my_string = "1. 2. 3. 4. 5. 6"
print(my_string.split(". "))

full_name = "Kim, Yuna"
name_data = full_name.split(", ")
last_name = name_data[0]
first_name = name_data[1]

print(first_name,last_name)

# 화이트 스페이스를 없애고 싶으면 split 파라미터 넣지 말기!
numbers = "     \n\n    2   \t    3  \n  5 7 11 \n\n".split()
print(int(numbers[0])+int(numbers[1])) #split을 이용하였을 때 리스트의 값은 모두 문자열!!

# 코딩에 빠진 닭
# 여기에 코드를 작성하세요
in_file = open('data/chicken.txt','r') 

total_revenue = 0
total_days = 0

for line in in_file:
    data = line.strip().split(": ")
    revenue = int(data[1])  # 그날의 매출
    total_revenue += revenue
    total_days += 1
print(total_revenue / total_days)

with open('new_file.txt','w') as f:
    f.write("Hello world!\n")
    f.write("My name is Codeit.")

# 추가
with open('new_file.txt','a') as f:
    f.write("Hello world!\n")
    f.write("My name is Codeit.\n")

# 6. 단어장 만들기
with open('vocabulary.txt', 'w') as f:
    while True:
        english_word = input('영어 단어를 입력하세요: ')    
        if english_word == 'q':
            break
        
        korean_word = input('한국어 뜻을 입력하세요: ')
        if korean_word == 'q':
            break
        
        f.write('{}: {}\n'.format(english_word, korean_word))
        
# 7. 단어 퀴즈
with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        english_word, korean_word = data[0],data[1]
        guess = input("{}: ".format(korean_word))

        if guess == english_word:
            print("맞았습니다!")
        else :
            print("아쉽습니다. 정답은 {}입니다.".format(english_word))
            
# 8. 고급 단어장
import random

# 사전 만들기
vocab = {}
with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]
        vocab[english_word] = korean_word

# 목록 가져오기
keys = list(vocab.keys())

# 문제 내기
while True:
    # 랜덤한 문제 받아 오기
    index = random.randint(0, len(keys) - 1)
    english_word = keys[index]
    korean_word = vocab[english_word]
    
    # 유저 입력값 받기
    guess = input("{}: ".format(korean_word))
    
    # 프로그램 끝내기
    if guess == 'q':
        break
    
    # 정답 확인하기
    if guess == english_word:
        print("정답입니다!\n")
    else:
        print("틀렸습니다. 정답은 {}입니다.\n".format(english_word))


