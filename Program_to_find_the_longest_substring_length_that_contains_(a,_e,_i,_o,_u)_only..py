a=input()
b="aeiou"
k=[]
s=0
for i in a:
    if i in b:
        s+=1
    else:
        k.append(s)
        s=0
k.append(s)
print(max(k))