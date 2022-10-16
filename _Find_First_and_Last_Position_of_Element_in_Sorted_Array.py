a=int(input())
b=list(map(int,input().split()))
c=int(input())
k=[]
for i in range(a):
    if b[i]==c:
        k.append(i)
        break
for j in range(1,a+1):
    if b[-j]==c:
        m=a-j
        k.append(m)
if len(k)==1:
    print(k[0],k[0])
elif len(k)>=2:
    print(k[0],k[1])
else:
    print("-1","-1")
    