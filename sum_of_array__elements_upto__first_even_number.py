a=int(input())
b=list(map(int,input().split()))
s=[]
for i in b:
    if i%2==0:
        break
    else:
        s.append(i)
print(sum(s))