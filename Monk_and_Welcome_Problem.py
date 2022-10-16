a=int(input())
b=list(map(int,input().split()))
c=list(map(int,input().split()))
k=[]
for i in range(a):
    s=b[i]+c[i]
    k.append(s)
print(*(k))