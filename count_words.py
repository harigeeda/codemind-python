a=input()
b="aeiouAEIOU"
s=0
for i in (a.split()):
    if i[0] in b and i[-1] not in b:
        s+=1
print(s)