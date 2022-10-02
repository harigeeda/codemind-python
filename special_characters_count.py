a=input()
s=0
b="abcdefghijklmnopqrstuvwxyz"
c="ABCDEFGHIJKLMNOPRSTUVWXYZ"
d=" "
for i in a:
    if i not in b and i not in c and i not in d:
        s+=1
print(s)