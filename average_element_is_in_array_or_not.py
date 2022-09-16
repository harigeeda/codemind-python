a=int(input())
b=list(map(int,input().split()))
c=sum(b)
d=c//a
print(d in b)