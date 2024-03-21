n, m  = map(int, input().split())
ball = []
for i in range(n):
    ball.append(0)

for _ in range(m):
    i, j, k = map(int, input().split())
    for n in range(i, j+1):
        ball[n-1] = k

for i in ball:
    print(i, end=' ')
    
n, m  = map(int, input().split())
ball = []
for i in range(n):
    ball.append(i+1)
for _ in range(m):
    i, j= map(int, input().split())
    a = ball[i-1]
    ball[i-1] = ball[j-1]
    ball[j-1] = a
    
print(*ball)

n, m  = map(int, input().split())
basket = []
for i in range(n):
    basket.append(i+1)
for _ in range(m):
    i, j= map(int, input().split())
    basket[i-1:j] = basket[i-1:j][::-1]
    
print(*basket)

n = int(input())

for i in range(1,n+1):
    print(" "*(n-i) + "*"*(2*i-1))
    
n = int(input())

for i in range(1,n+1):
    print(" "*(i-1) + "*"*((2*n)-(2*i-1)))
for i in range(1,n):
    print(" "*(n-(i+1)) + "*"*(2*i+1))
   
submit = []  
for i in range(28):
    submit.append(i)
    submit[i] = int(input())
    
not_submit = []
for i in range(1,31):
    if i not in submit:
        not_submit.append(i)
print(min(not_submit))
print(max(not_submit))

n = int(input())

score = map(int, input().split())
s_list = list(score)
score_max = max(s_list)

new_score = []
for i in range(n):
    a = s_list[i]/score_max*100
    new_score.append(a)
hap = 0
for i in range(n):
    hap += new_score[i]
print(hap/n)
    

divide = []
for i in range(10):
    divide.append(i)
    a = int(input())
    divide[i] = a

answer = []
for i in range(10):
    b = divide[i] % 42
    answer.append(b)
    
result = []
for value in answer:
    if value not in result:
        result.append(value)
    
print(len(result))   

right = [1, 1, 2, 2, 2, 8]
dong = list(input().split())
answer = []
for i in range(6):
    if int(right[i]) - int(dong[i])> 0:
        answer.append(int(right[i]) - int(dong[i]))
    elif int(right[i]) - int(dong[i]) < 0:
        answer.append(int(right[i]) - int(dong[i]))
    else :
        answer.append(0)
print(*answer)

n = int(input())
for i in range(n):
    print(" "*i +"*"*(2*n-(2*i+1)))

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    for i in range(max(a,b),(a*b+1)):
        if i % a == 0 and i % b == 0:
            print(i)
            break
        
import math
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(math.lcm(a,b))

i = 0
while True :
    a = int(input())
    if a == 0:
        break
    b = str(a)
     
    if b == b[::-1]:
        print("yes")
    else :
        print("no")
    i += 1      
       
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i) + "*"*(i))
for i in range(1,n):
    print(" "*(i) + "*"*(n-i))
    
n = int(input())
for i in range(1,n+1):
    print("*"*i + " "*(2*n-2*i)+ "*"*i)
for i in range(1,n):
    print("*"*(n-i) + " "*(2*i)+ "*"*(n-i))
    
def Rev(num):
    num = str(num)
    num_rv = num[::-1]
    return num_rv
          
x, y = map(int, input().split())
rev_x = Rev(x)
rev_y = Rev(y)
hap = int(rev_x) + int(rev_y)
print(int(Rev(hap)))

   
import math
a, b = map(int, input().split())
print(math.gcd(a,b))
print(math.lcm(a,b))

n = int(input())
for i in range(1,n+1):
    print("*"*i)
for i in range(1,n):  
    print("*"*(n-i))    

import sys
n= int(input())

hap = 0
for i in range(1, sys.maxsize):
    if i % n == i // n:
        hap += i
        
print(hap)

a, b = map(int, input().split())
print(a/b)

word = input().split()
print(len(word))    

n = input()
num = ''
for i in range(1,100000):
    num += str(i)
    
for j in len(num):
    if num[j] == n:
        print(j)
    else :
        pass
    
T = int(input())
for i in T:
    num = input()
    num_rv = num[::-1]
    
    hap = int(num) + int(num_rv)
    hap_str = str(hap)
    hap_rv = hap_str[::-1]
    
    hap = str(hap)
    hap_rv = str(hap_rv)
    
    for j in (len(hap)//2):
        if hap[j] == hap_rv[-(j+1)]:
            print("YES")
        else:
            print("NO") 

import math
t = int(input())
n = int(input())
for i in range(t):
    a=math.factorial(n)

    if a % 10 == 0:
        a /= 10
        a = int(a)
    else:
        a = str(a)
        print(a[-1])

import math
a, b = map(int, input().split())
print(math.lcm(a,b)) 

n = int(input())
name = input()

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

hap = 0
for i in range(n):
    a = alpha.index(name[i]) + 1
    hap += a
    
print(hap)

# 핸드폰 번호 궁합(17202)
import itertools as it
a = input()
b = input()
hap = list(it.chain(*zip(a,b)))

while len(hap) != 2:
    temp = []
    for i in range(len(hap)-1):
        a = (int(hap[i])+int(hap[i+1])) % 10
        temp.append(a)
    hap = temp

result = ''.join(map(str, hap))
print(result)

s = input()
a = s.split(',')
print(len(a))



T = int(input())
            
for i in range(T):
    n, m = map(int, input().split())
    count = 0
    for j in range(n,m+1):
        w = str(j)
        count += w.count('0')
    print(count)

import sys

N = int(sys.stdin.readline())
arr = [0] * 10001

for i in range(N):
    arr[int(sys.stdin.readline())] += 1
for i in range(len(arr)):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)          

croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input()

for i in croatia:
    word = word.replace(i,'*')
print(len(word))

import sys
a,b = map(int,sys.stdin.readline().split())
print(a/b)

a, b, c = map(int, input().split())
list = [a,b,c]
k = max(list)
list.remove(k)
print(max(list))



num = int(input())
re_num = num
t = 0
while True:
    a = num // 10
    b = num % 10
    c = a + b
    d = str(b) + str(c%10)
    num = int(d)
    t += 1

    if (re_num == num):
      print(t)
      break

import sys  
T = int(input())

for i in range(T):
    result = []
    test = sys.stdin.readline().split()
    for j in range(len(test)):
        word = test[j]
        result.append(word[::-1])
    print(' '.join(result))

import sys  
T = int(input())
for i in range(T):
    a,b = map(int, sys.stdin.readline().split(','))
    print(a+b)

k = int(input())
a = 1
b = 0
for i in range(1,k+1):
    a_r = a
    a = b
    b = a_r + a
print(a, b)

s = ''
while True:
    try:
        s += input().strip()
    except:
        break
print(sum(map(int, s.split(','))))

a,b = map(int, input().split())
ls = []
for i in range(1,b+1):
    for j in range(i):
        ls.append(i) 
hap = []
for i in range(a-1,b):
    a = ls[i]
    hap.append(a)
    
hap_list = sum(hap)
print(hap_list)
        
while True:
    try:
        print(input())
    except:
        break


import sys    
C = int(sys.stdin.readline())
li = []
for i in range(C):
    li = list(map(int,sys.stdin.readline().split()))
    
    sum = 0
    avg = 0
    count = 0
    for j in range(1, len(li)):
        sum += li[j]
    avg = sum / li[0]

    for k in range(1, len(li)):
        if li[k] > avg:
            count += 1
    result = round(count*100 / li[0],3)
    print(f'{result:.3f}%')
    li.clear()

sum = 0
for i in range(5):
    a = int(input())
    if a < 40:
        a = 40
    sum += a
print(int(sum/5))

a,b = map(str, input().split())
a_ls = []
b_ls = []
for i in range(2,-1,-1):
    a_ls.append(a[i])
    b_ls.append(b[i])
a = int(''.join(a_ls))
b = int(''.join(b_ls))

if a > b:
    print(a)
else:
    print(b)
    
a = int(input())
b = int(input())
c = int(input())

result = a * b * c
result_l = list(map(int, str(result)))
for i in range(10):
    print(result_l.count(i))

a = int(input())
s = input()
b = int(input())

if s == '+':
    print(a+b)
elif s == '*':
    print(a*b)

x = []
y = []
for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
x_l = []
if x[0] == x[1]:
    x_l.append(x[2])
elif x[0] > x[1]:
    x_l.append(x[1])
elif x[0] < x[1]:
    x_l.append(x[0])
else:
    pass
y_l = []
if y[0] == y[1]:
    y_l.append(y[2])
elif y[0] > y[1]:
    y_l.append(y[1])
elif y[0] < y[1]:
    y_l.append(y[0])
else:
    pass

arr = []
for _ in range(3):
    arr.append(list(map(int, input().split())))
    
arr.sort()
x=0
y=0

if arr[0][0]==arr[1][0]:
    x = arr[2][0]
elif arr[1][0] == arr[2][0]:
    x = arr[0][0]
else : 
    x = arr[1][0]
    
if arr[0][1]==arr[1][1]:
    y = arr[2][1]
elif arr[1][1] == arr[2][1]:
    y = arr[0][1]
else : 
    y = arr[1][1]
print(x,y)

def solve(a):
    return sum(a)

a = [1,2,3,4,5,6,7,8,9,10]

N = int(input())
if N == 1:
    print("*")
else:
    for i in range(N):
        if i % 2 != 0:
            print(" *"*N)
        else:
            print("* "*N)
            
word = input().lower()
word_list = list(set(word))
cnt = []
for i in word_list:
    count = word.count(i)
    cnt.append(count)
if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))].upper())
    
T = int(input())
for i in range(T):
    R, S = input().split()
    R = int(R)
    for j in range(len(S)):
        print(S[j]*R, end='')
    print("")
    
N = int(input())
for i in range(N*2):
    if N == 1:
        print("*")
        break
    else:
        if N % 2 != 0:
            if i % 2 == 0:
                print("* "*int((N+1)/2))
            else:
                print(" *"*int(N/2))
        else:
            if i % 2 == 0:
                print("* "*int(N/2))
            else:
                print(" *"*int(N/2))
    
import statistics
import sys
ls = []
for i in range(5):
    a = int(sys.stdin.readline())
    ls.append(a)
print(int(sum(ls)/5))
print(statistics.median(ls))
    
import statistics
import sys
ls = []
for i in range(10):
    a = int(sys.stdin.readline())
    ls.append(a)   
print(int(sum(ls)/10)) 
print(statistics.mode(ls))


import sys
N = int(input())
for i in range(N):
    a = sys.stdin.readline()
    a = a[0].upper()+a[1:]
    print(a,end='')
    
T = int(input())
for i in range(T):
    N = int(input())
    ls = list(map(int, input().split()))
    print(min(ls),max(ls))


T = int(input())
for i in range(T):
    ls = list(map(int, input().split()))
    ls.sort()
    print(ls[-3])
        

word = input()
for i in range(0,len(word),10):
    print(word[i:i+10])
    
s = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha_list = [-1]*26

for i in s:
    alpha_list[alpha.index(i)] = s.index(i)
    
for i in alpha_list:
    print(i, end=' ')
    
n = int(input())
s = "%.300f" % 2 ** - n
end = len(s)
for i in range(end-1,1,-1):
    if s[i] != '0':
        end = i
        break
print(s[:end+1])


def self(N):
    print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
    for i in range(N):
        print('____'*i, end='')
        print('"재귀함수가 뭔가요?"')
        print('____'*i, end='')
        print('"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print('____'*i, end='')
        print("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
        print('____'*i, end='')
        print('그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        
    print('____'*(i+1), end='')
    print('"재귀함수가 뭔가요?"')
    print('____'*(i+1), end='')
    print('"재귀함수는 자기 자신을 호출하는 함수라네"')
        
    for i in range(N,-1,-1):
        print('____'*i, end='')
        print("라고 답변하였지.")
             
N = int(input())
self(N)

N = int(input())
for i in range(N,0,-1):
    print(i)

minkook = list(map(int, input().split()))
manse = list(map(int, input().split()))
S = sum(minkook)
T = sum(manse)
if S > T:
    print(S)
elif S < T:
    print(T)
else:
    print(S)

a, b, c = map(int, input().split())
if b >= c:
    print(-1)
else:
    print(a//(c-b)+1)
    
import math
n, k = map(int, input().split())
result = math.factorial(n)/(math.factorial(n-k) * math.factorial(k))
print(int(result))

T = int(input())
for i in range(T):
    score = list(map(int, input().split()))
    
    if max(score)- min(score) > 5 :
        print("KIN")
    else :
        score.remove(max(score))
        score.remove(min(score))
        print(sum(score))

import math    
a, b, v = map(int, input().split())
day = (v-b) / (a-b)
print(math.ceil(day)) # 반올림

import sys
N = int(sys.stdin.readline()) 
ls = [int(sys.stdin.readline()) for _ in range(N)]
ls.sort(reverse=True)
for i in ls:
    print(i)

pitch = '1 2 3 4 5 6 7 8'
pitch_rv = '8 7 6 5 4 3 2 1'
x = str(input())

if x == pitch:
    print("ascending")
elif x == pitch_rv:
    print("descending")
else:
    print("mixed")

# 소인수분해
N = int(input())
while N >= 2:
    for i in range(2, N+1):
        if N % i == 0:
            print(i)
            break
    N = N//i
    
ls = [int(input()) for _ in range(9)]
ls.sort()
sum_n = sum(ls)
# 모두 다 더하고 2명 뺐을 때, 그 값이 100
for i in range(len(ls)):
    for j in range(i+1, len(ls)):
        if sum_n -ls[i]-ls[j] == 100:
            for k in range(len(ls)):
                if k == i or k == j:
                    pass
                else:
                    print(ls[k])
            exit()
# 2839
n = int(input())

if n % 5 == 0:
    print(n//5)
else:
    p = 0
    while n > 0:
        n -=3
        p += 1
        if n % 5== 0: # 3과 5를 조합해서 담을 수 있을 때
            p += n//5
            print(p)
            break
        elif n ==1 or n == 2: # 나눌 수 없을 때
            print(-1)
            break
        elif n == 0 : # 3으로 나누어 떨어질 때
            print(p)
            break

# 1225   
import sys
a,b = map(list, sys.stdin.readline().split())  
a = list(map(int,a))
b = list(map(int,b))
print(sum(a)*sum(b))

# 4153
while True:
    num= list(map(int, input().split()))
    
    if sum(num) == 0:
        break
    max_num = max(num)
    num.remove(max_num)
    if num[0]**2 + num[1]**2 == max_num**2:
        print('right')
    else:
        print('wrong')
        
# 1920
'''시간초과
N = int(input())
first_ls = list(map(int, input().split()))
M = int(input())
second_ls = list(map(int, input().split()))
for i in range(M):
    if second_ls[i] in first_ls:
        print(1)
    else:
        print(0)
'''

N = int(input())
first_ls = set(map(int, input().split())) # 탐색시간을 줄이기 위해 set으로 받음

M = int(input())
second_ls = list(map(int, input().split()))

for i in range(M):
    if second_ls[i] in first_ls:
        print(1)
    else:
        print(0)
        
# 10773
ls = []
K = int(input())
for i in range(1,K+1):
    num = int(input())
    if num == 0:
        ls.pop()
    else:
        ls.append(num)
print(sum(ls))

# 10845
from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
dq = deque()

for _ in range(N):
    command = list(input().split())
    if command[0] == 'push':
        dq.append(command[1])
    elif command[0] == 'pop':
        if len(dq) > 0 :
            tmp = dq.popleft()
            print(tmp)
        else : print(-1)
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty':
        if len(dq) > 0 :
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if len(dq)>0:
            print(dq[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if len(dq)>0:
            print(dq[-1])
        else:
            print(-1)

# 15688
import sys
N = int(sys.stdin.readline())
ls = []
for i in range(N):
    ls.append(int(sys.stdin.readline()))
for i in sorted(ls):
    print(i)

# 10814
N = int(input())
user = []
for _ in range(N):
    age, name = map(str, input().split())
    user.append([int(age),name])

user = sorted(user, key=lambda x: x[0])

for i in user:
    print(*i)