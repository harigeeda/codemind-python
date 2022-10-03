a=int(input())
b=list(map(int,input().split()))
for i in b:
    k=str(abs(i))
    print(len(k),end=" ")