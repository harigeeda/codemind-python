a=input()
b=len(a)
even=0
odd=0
for i in range(0,b):
    if int(a[i])%2==0:
        even+=1
    if int(a[i])%2!=0:
        odd+=1
if even>0 and odd==0:
    print("Even")
elif even==0 and odd>0:
    print("Odd")
else:
    print("Mixed")