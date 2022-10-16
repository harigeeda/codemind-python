a=int(input())
b=list(map(int,input().split()))
k=[]
for i in range(1,a):
    c=b[i:]
    k.append(max(c))
k.append("-1")
print(*(k))