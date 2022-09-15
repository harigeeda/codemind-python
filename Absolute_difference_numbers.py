a=input()
b=len(a)
c=int(a[-1])
d=(b-2)-c
x=int(a[:c])
y=int(a[d:-2])
print(abs(x-y))