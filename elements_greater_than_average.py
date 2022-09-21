a=int(input())
b=list(map(int,input().split()))
s=0
d=sum(b)//a
for i in range(0,a):
    if b[i]>=d:
        s+=1
print(s)