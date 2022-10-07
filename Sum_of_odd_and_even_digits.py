a=int(input())
b=list(map(int,input().split()))
even=[]
odd=[]
for i in range(0,a):
    if i%2==0:
        even.append(b[i])
    else:
        odd.append(b[i])
c=sum(odd)-sum(even)
if c==0:
    print("YES")
else:
    print("NO")