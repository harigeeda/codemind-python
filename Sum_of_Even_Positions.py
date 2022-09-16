a=int(input())
b=list(map(int,input().split()))
s=0
for i in range(0,a):
    if i%2==0:
        s+=int(b[i])
print(s)
