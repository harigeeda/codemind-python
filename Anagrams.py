a=input()
b=input()
a=a.lower()
b=b.lower()
c=(set(a))
d=(set(b))
s=0
k="qwertyuiplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM"
for i in c:
    if i in d:
        if i in k:
            s+=0
    else:
        s+=1
for j in d:
    if j in c:
        if j in k:
            s+=0
    else:
        s+=1
print(s==0)
        