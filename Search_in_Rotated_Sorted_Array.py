a=int(input())
b=list(map(int,input().split()))
c=int(input())
if c in b:
    print(b.index(c))
else:
    print("-1")