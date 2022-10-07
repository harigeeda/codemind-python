a=input()
b="aeiou"
k=0
s=[]
for i in (a.split()):
    for j in i:
        if j in b:
            k+=1
    s.append(k)
    k=0
print(min(s))
