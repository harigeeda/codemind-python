a=int(input())
b=int(input())
for i in range(a,b+1):
    k=str(i)
    if k==k[::-1]:
        print(i,end=" ")