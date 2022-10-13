a=int(input())
x=list(map(int,input().split()))
b=int(len(x)/2)
for i in range(b,0,-1):
    k=x[-i]
    x.insert(0,k)
print(*(x[:-b]))