a=input()
b=len(a)
s=""
for i in range(1,b+1):
    s+=a[-i]
print(s==a)