a=input()
s=[]
b="aeiouAEIOU"
for i in a:
    if i in b and i not in s:
        s.append(i)
print(*s)