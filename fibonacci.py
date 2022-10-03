a=int(input())
b=0
c=1
for i in range(a):
    print(b,end=" ")
    temp=b
    b=c
    c=(c+temp)