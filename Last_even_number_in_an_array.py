a=int(input())
b=list(map(int,input().split()))
s=[]
for i in range(0,a):
    for i in b:
        if i%2==0:
            s.append(i)
print(s[-1])
    