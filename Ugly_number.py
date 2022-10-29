def prime(x):
    if x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
a=int(input())
b=[]
for i in range(1,a+1):
    if a%i==0 and prime(i):
        b.append(i)
if a<0:
    print("Not Ugly Number")
elif a==1:
    print("Ugly Number")
elif max(b)<=5:
    print("Ugly Number")
else:
    print("Not Ugly Number")
