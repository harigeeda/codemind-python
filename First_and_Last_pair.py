import math
a=int(input())
a1=a//2
b=list(map(int,input().split()))
s=[]
j=[]
for i in range(0,a1):
    c=i+1
    s.append(b[i])
    s.append(b[-c])
if a%2!=0:
    m=math.floor(a/2)
    k=(b[m])
    j.append(k)
    j.append(0)
    m1=s+j
    print(*(m1))
else:
    print(*(s))