a=input()
b=list(map(int,input().split()))
c=[]
d=[]
for i in b:
    if i==0:
        c.append("0")
    if i==1:
        d.append("1")
print(*(c+d))