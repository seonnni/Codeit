a, b=input().split()
print(int(a)+int(b))
print(int(a)-int(b))
print(int(a)*int(b))
print(int(a)//int(b))
print(int(a)%int(b))

id = input()
print(id+'??!')

year= input()
print(int(year)-543)

a,b,c = map(int, input().split())
print((a+b)%c)
print(((a%c)+(b+c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)

a=int(input())
b=int(input())
print(a*(b%10))
print(a*((b%100)//10))
print(a*(b//100))
print(a*b)

a,b,c = map(int, input().split())
print(a+b+c)

print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")

print("|\\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\\__|")
    

a,b = map(int, input().split())
if a>b :
    print('>')
elif a<b :
    print('<')
else:
    print('==')

a = int(input())
if a>= 90 and a<=100 :
    print("A")
elif a>=80 and a<=89 :
    print("B")
elif a>=70 and a<=79 :
    print("C")
elif a>=60 and a<=69 :
    print("D")
else
    print("F")
    
