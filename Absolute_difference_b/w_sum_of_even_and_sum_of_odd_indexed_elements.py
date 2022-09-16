a=int(input())
b=list(map(int,input().split()))
s=0
y=0
for i in range(0,a):
    if i%2==0:
        s+=int(b[i])
    else:
        y+=int(b[i])
print(abs(s-y))