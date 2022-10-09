a=int(input())
b=list(map(int,input().split()))
s=0
for i in range(0,a):
    if b[i]%2==0:
        if i%2==0:
            s+=0
        else:
            s+=1
print(s==0)
    