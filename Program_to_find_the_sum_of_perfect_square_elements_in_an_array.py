import math
a=int(input())
b=list(map(int,input().split()))
s=0
for i in b:
    c=i**0.5
    if c==math.ceil(c):
        s+=i
print(s)