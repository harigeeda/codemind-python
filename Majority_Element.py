import math
a=int(input())
b=list(map(int,input().split()))
c=(a/2)
k=[]
for i in b:
    if i not in k:
        k.append(i)
for j in k:
    if b.count(j)>c:
        print(j)
        break