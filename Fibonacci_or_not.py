a=int(input())
b=0
c=1
s=[]
for i in range(a):
    s.append(b)
    temp=b
    b=c
    c=(c+temp)
print(a in s)