a=input()
b=a.lower()
s=0
for i in (b.split()):
    if i==i[::-1]:
        s+=1
print(s)