import math
a=int(input())
b=list(map(int,input().split()))
c=a%2
d=[]
if c!=0:
    for i in range(0,(a-1)):
        d.append(b[i])
    d.append(b[-1])
    d.append("0")
if c!=0:
    print(*(d))
else:
    print(*(b))

        