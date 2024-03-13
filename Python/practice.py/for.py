n = int(input())
for i in range(1,10):
    print(n, '*', i, '=', n*i)
    
T = int(input())
for i in range(T):
    a,b = map(int, input().split())
    print(a+b)
    
n = int(input())
hap=0
for i in range(1,n+1) :
    hap = hap +i
print(hap)

X = int(input())
N = int(input())
sum = 0
for i in range(N):
    a,b = map(int, input().split())
    c = a*b
    sum = sum + c
if sum == X :
    print("Yes")
else:
    print("No")
    
a = int(input())
n = a//4
print("long "*n+"int")

import sys
T = int(input())
for i in range(T):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)
    
T = int(input())
for i in range(T):
    a,b = map(int, input().split())
    print("Case #{}: {}".format(i+1,a+b))
    
T = int(input())
for i in range(T):
    a,b = map(int, input().split())
    print("Case #{}: {} + {} = {}".format(i+1,a,b,a+b))
    
N = int(input())
for i in range(N):
    print("*"*(i+1))
    
N = int(input())
for i in range(N):
    print(" "*(N-(i+1)) +"*"*(i+1))
    

while True:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except:
        break
  
