a=int(input())
b=list(map(int,input().split()))
s=0
for i in range(0,(a-1)):
    if b[i]<b[i+1]:
        s+=0
    else:
        s+=1
if s==0:
    print("yes")
else:
    print("no")