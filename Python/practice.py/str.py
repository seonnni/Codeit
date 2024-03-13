S= input()
i = int(input())
print(S[i-1])

a = input()
print(len(a))

import sys
x = int(input())
for i in range(x):
    s = str(sys.stdin.readline())
    a = s[0]
    b = s[-2]
    print("{}{}".format(a,b))
    
a = input()
print(ord(a))   

input()
print(sum(map(int, input())))

print("         ,r'\"7")
print("r`-_   ,'  ,/")
print(" \\. \". L_r'")
print("   `~\\/")
print("      |")
print("      |")

n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))
for i in range(n-1,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))


word = input()

if all(word[i]==word[-i-1] for i in range(len(word)//2)):
    print(1)
else:
    print(0)

def is_palindrome(word):
        if all(word[i] == word[-(i+1)] for i in range((len(word)//2))):
            return True
        else :
            return False
             
s = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha_list = [-1]*26
idx = 0

for i in s:
    if alpha_list[alpha.index(i)]>-1:
        pass
    else:
        alpha_list[alpha.index(i)] = idx
        idx += 1
    
for i in alpha_list:
    print(i, end=' ')
            
n = int(input())
for i in range(n):
    print(" "*i + "*"*(n-i)) 

n = int(input())
for i in range(n):
    print("*"*(n-i))           
        
     
    

       



