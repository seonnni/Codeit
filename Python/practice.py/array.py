n = int(input())
num_list = list(map(int, input(). split()))
v = int(input()) 
print(num_list.count(v))  

n, x = map(int,input().split())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] < x :
        print(a[i],end=" ")
    else :
        pass

n = int(input())
a = list(map(int, input().split()))
print(min(a), max(a))   
# 최솟값
min = 0
if a[i] < a[i+1]:
    min = a[i]
else :
    min = a[i+1]
for i in range(n-1):
    if min < a[i+2]:
        i += 1
    else :
        min = a[i+2]


# 최댓값
max = 0
if a[i] > a[i+1]:
    max = a[i]
else:
    max = a[i+1]
    
for i in range(n-1):
    if max > a[i+2]:
        i += 1
    else :
        max = a[i+2]

print(min,max)

a= []
for i in range(9):
    x = int(input())
    a.append(x)
    
print(max(a))
print(a.index(max(a))+1)

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
    
