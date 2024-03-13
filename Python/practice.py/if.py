a = int(input())
if a>= 90 :
    print("A")
elif a>=80 :
    print("B")
elif a>=70 :
    print("C")
elif a>=60 :
    print("D")
else :
    print("F")
    
a = int(input())
if a % 4 ==0 and a % 100 != 0:
    print("1")
elif a % 400 == 0:
    print("1")
else: 
    print("0")
    
a = int(input())
b = int(input())
if a>0 and b>0:
    print("1")
elif a<0 and b>0:
    print("2")
elif a<0 and b<0:
    print("3")
else :
    print("4")

h, m = map(int, input().split())
if h==0:
    if m<45:
        print(h+23,m+15)
    else :
        print(h,m-45)
else:
    if m<45:
        print(h-1,m+15)
    else :
        print(h,m-45)
 
a, b = map(int, input().split())
c= int(input())
h= c//60
m= c%60
a= a+h
b= b+m
if b>=60:
    a = a+1
    b = b-60
    if a >= 24:
        a = a-24
        print(a,b)
    else:
        print(a,b)
else :
    if a>=24 :
        a = a-24
        print(a,b) 
    else :
        print(a,b) 
    
a, b, c = map(int, input().split())
if a==b==c :
    print(10000+a*1000)
elif a==b or b==c or a==c :
    if a==b:
        print(1000+a*100)
    elif b==c:
        print(1000+b*100)
    else  :
        print(1000+a*100)
else:
    if a>b and a>c :
        print(a*100)
    elif b>a and b>c :
        print(b*100)
    else:
        print(c*100)