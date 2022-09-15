a=input()
x=len(a)
b=0
c=1
for i in range(0,x):
    b+=int(a[i])
    c*=int(a[i])
print(abs(b-c))