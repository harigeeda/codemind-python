n=int(input())
if n<0:
    a=abs(n)
else:
    a=n
s=0
l=10**(len(str(a))-1)
while a:
    r=a%10
    s+=l*r
    l//=10
    a//=10
if n<0:print(-1*s)
else:print(s)