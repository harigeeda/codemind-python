a=int(input())
b=int(input())
k=[]
s=0
for i in range(a):
    m=list(map(int,input().split()))
    k.append(m)
for l in k:
    for n in l:
        s+=n
print(s)